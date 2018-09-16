# Code based on Dan Shiebler's RBM music generator: https://github.com/dshieble/Music_RBM

import tensorflow as tf
import numpy as np
from utils import rbm
from tensorflow.python.ops import control_flow_ops
from utils import midi_manipulation
from tqdm import tqdm


num_timesteps = rbm.num_timesteps
x, emotions, W, bh, bv = rbm.get_variables()

def sample(probs):

	return tf.floor(probs + tf.random_uniform(tf.shape(probs), 0, 1))


def sample_correct(probs, emotions):

	notes = tf.floor(probs + tf.random_uniform(tf.shape(probs), 0, 1))[0]
	notes = tf.unstack(notes)
	emotions = tf.unstack(emotions)
	print(len(emotions))
	for i in range(16):
		j=156
		e = int(i/2)
		notes[j] = emotions[e]
		if(e+1 < len(emotions)):
			notes[j+1] = emotions[e+1]
		else:
			notes[j+1] = emotions[len(emotions) - 1]
		j += 158
	notes = tf.stack(notes)
	final = tf.cast(notes, tf.float32)
	final = tf.reshape(final, [1, 10112])
	return final


def gibbs_sample_generate(k):

	def gibbs_step_generate(count, k, xk):

		hk = sample(tf.sigmoid(tf.matmul(xk, W) + bh)) # Propagate the visible values to sample the hidden values
		tv = tf.matmul(hk, tf.transpose(W)) + bv	   # Propagate the hidden values to the visible values
		xk = sample_correct(tf.sigmoid(tv), emotions)  # sample the visible values and clamp emotion values
		return count+1, k, xk

	x_sample = x
	# run gibbs steps for k iterations
	ct = tf.constant(0)
	[_, _, x_sample] = tf.while_loop(lambda count, num_iter, *args: count < num_iter,
										 gibbs_step_generate, [ct, tf.constant(k), x_sample])
	x_sample = tf.stop_gradient(x_sample) 
	return x_sample


def generate_music(emotion_text_file, midi_file_name):

	tf.reset_default_graph()
	saved_weights_path = "/utils/parameter_checkpoints/trained_system"	  # path to saved, trained model
	trainable_vars = [W, bh, bv]
	n_visible = rbm.n_visible
	note_range = midi_manipulation.span
	saver = tf.train.Saver(trainable_vars) # restore the weights and biases of the model
	with tf.Session() as sess:
		init = tf.initialize_all_variables()
		sess.run(init)
		print("hi")
		saver.restore(sess, saved_weights_path) # load the saved weights and biases of the model
		
		print("hi3")
		text = open(emotion_text_file, 'r')		
		x_ = np.zeros((1, n_visible))
		j=156
		emotions_ = np.array([])

		# iterate through each line of the emotion text file
		for l, line in enumerate(text):
			emotion = line[:-1].split(",")
			a = float(emotion[0])		# arousal value
			v = float(emotion[1])		# valene value
			e = np.array([a,v])
			emotions_ = np.concatenate((emotions_, e), axis=0)
			for i in range(16):
				x_[0][j] = a
				x_[0][j+1] = v
				j += 158

			if l%4==3:
				# sample by running Gibbs chain 10 times
				sample = gibbs_sample_generate(10).eval(session=sess, feed_dict={x: x_, emotions: emotions_})

				# reshape the vector to be timesteps x notes (64x158), and then keep adding into one final matrix (song) 
				if 'song' in locals():
					S = np.reshape(sample, (num_timesteps, (2*note_range+2)))
					song = np.concatenate((song, S), axis=0)
				else:
					song = np.reshape(sample, (num_timesteps, (2*note_range+2)))
				
	
				x_ = np.zeros((1, n_visible))

				emotions_ = np.array([])
				j=156

		# save the matrix as a midi file
		midi_manipulation.noteStateMatrixToMidi(song, midi_file_name)
	return

if __name__ == "__main__":
	generate_music("/Users/Joel/Desktop/hr8/sentiment_files/bh.txt", "/Users/Joel/Desktop/hr8/midi/bh.midi")
