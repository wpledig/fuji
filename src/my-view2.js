/**
 * @license
 * Copyright (c) 2016 The Polymer Project Authors. All rights reserved.
 * This code may only be used under the BSD style license found at http://polymer.github.io/LICENSE.txt
 * The complete set of authors may be found at http://polymer.github.io/AUTHORS.txt
 * The complete set of contributors may be found at http://polymer.github.io/CONTRIBUTORS.txt
 * Code distributed by Google as part of the polymer project is also
 * subject to an additional IP rights grant found at http://polymer.github.io/PATENTS.txt
 */

import { PolymerElement, html } from '@polymer/polymer/polymer-element.js';
import './shared-styles.js';

class MyView2 extends PolymerElement {
  static get template() {
    return html`
      <style>
        :host {
          display: block;
          padding: 10px;
        }
        .question-list {
        text-align: center;
        }
        
        .holder {
           width: 70%;
        margin-top: 20px;
                  padding: 16px;
          text-align: center;
          display: inline-block;
          color: #757575;
          border-radius: 5px;
          background-color: #fff;
          box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.14), 0 1px 5px 0 rgba(0, 0, 0, 0.12), 0 3px 1px -2px rgba(0, 0, 0, 0.2);
        
        }
        
        .question {
          font-size: 22px;
          font-weight: bold;
        }
        
        .answer {
            font-size: 15px;
        }
        video {
        display: inline-block;
        }
      </style>

        


    <div class="question-list">
      <div class="holder">
        <div class="question">What is TrackIT?</div>
        <div class="answer">TrackIT is a web-application that takes in a video and returns music dynamically generated to fit the video. It was developed by Will Ledig and Joel Abraham for HackRice 8.</div>
      </div>
      <div class="holder">
        <div class="question">Do you have any examples?</div>
        <div class="answer" style="margin-bottom: 10px;">Yes! Here are some examples we feel demonstrate the power of our application:</div>
        <video height="160" width="284" src="../mp4/test.mp4" controls style="padding-right: 60px;"></video>
        <video height="160" width="284" src="../mp4/test_edited.mp4" controls></video>
      </div>
      <div class="holder">
        <div class="question">How does it work?</div>
        <div class="answer">The application breaks down inputted videos frame by frame, averages the pixels across ranges of frames, and inputs that into a variety of APIs (including Microsoft Azure's Vision and Emotion APIs) to compile data on various time segments across the video's duration.
                            Once that is complete, this data is processed through a neural network to generate a MIDI file representative of the video's visuals.</div>
      </div>
      <div class="holder">
        <div class="question">How was it built?</div>
        <div class="answer">The entire front-end of the application was built in Polymer (a JavaScript library from Google for creating custom web components) 
        while the back-end was developed with Flask and Python, with the assistance of APIs such as Microsoft Azure's Vision and Emotion APIs, ______, and ______.</div>
      </div>
    </div>
    `;
  }


}

window.customElements.define('my-view2', MyView2);
