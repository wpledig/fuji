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
import './my-icons.js';
import '@polymer/iron-icon/iron-icon.js'
import '@vaadin/vaadin-upload/vaadin-upload.js';

class MyView1 extends PolymerElement {
  static get template() {
    return html`
      <style >
        :host {
          display: block;
          
          padding: 10px;
        }
        
        :host [part="drop-label"] {
          display: none;
        }
        
        #dropLabelContainer {
            display: none !important;
        }
        
        .card {
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
        .title-text {
          font-size: 30px;
          text-align: center;
          margin-top: 3%;
        }
        
        .upload {
        display: inline-block;
          height: 45px;
          width: 45px;
        }
        
        .empty {
        height: 0;
        width: 0;
        display: none;
        visibility: hidden;
        }
        
        .upload-label {
          font-size: 20px;
        }
        
        vaadin-upload {
            text-align: center;
            cursor: pointer;
            
        }
        
        .main {
        position: relative;
        text-align: center;
        }
        
      </style>
      <dom-module id="my-text-field" theme-for="vaadin-upload">
      <template is="dom-if" if="true">
        <style>
        [part="drop-label"], #dropLabelContainer {
            display: none !important;
        }
        </style>
      </template>
      </dom-module>

      <div class="main">
      <div class="title-text">Upload a video to generate background music!</div>

      <div class="card">
      
      
      <template is="dom-if" if="true">
        <style>
        vaadin-upload [part="drop-label"], #dropLabelContainer {
            display: none !important;
        }
        </style>
      </template>
        <vaadin-upload target="http://127.0.0.1:5000/upload" method="POST" timeout="300000" headers='{"Access-Control-Allow-Origin": "*", "Access-Control-Allow-Headers": "content-type"}' >
          
          <div slot="add-button" style="text-align: center; display: inline-block; margin-right: -14px;">
            <iron-icon class="upload" icon="my-icons:file-upload"></iron-icon>
            <div style="display: block; text-align: center;">Drop Files Here</div>
          </div>
          <div slot="drop-label-icon" class="empty"></div>
          <div slot="drop-label" class="empty"></div>
        </vaadin-upload>
        
      </div>
      </div>
      
    `;
  }
}

window.customElements.define('my-view1', MyView1);
