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
      </style>

        


    <div class="question-list">
      <div class="holder">
        <div class="question">What is TrackIT?</div>
        <div class="answer">TrackIT is a thing that does stuff. It was developed by Will Ledig and Joel Abraham for HackRice 8.</div>
      </div>
      <div class="holder">
        <div class="question">What is TrackIT?</div>
        <div class="answer">TrackIT is a thing that does stuff. It was developed by Will Ledig and Joel Abraham </div>
      </div>
      <div class="holder">
        <div class="question">What is TrackIT?</div>
        <div class="answer">TrackIT is a thing that does stuff. It was developed by Will Ledig and Joel Abraham </div>
      </div>
      <div class="holder">
        <div class="question">What is TrackIT?</div>
        <div class="answer">TrackIT is a thing that does stuff. It was developed by Will Ledig and Joel Abraham </div>
      </div>
    </div>
    `;
  }


}

window.customElements.define('my-view2', MyView2);
