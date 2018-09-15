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
      <style include="shared-styles">
        :host {
          display: block;
          
          padding: 10px;
        }
        .card {
          margin: 24px;
          position: absolute;
          text-align: center;
          top: 50%; left: 50%;
          transform: translate(-50%,-50%); 
          padding: 16px;
          color: #757575;
          border-radius: 5px;
          background-color: #fff;
          box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.14), 0 1px 5px 0 rgba(0, 0, 0, 0.12), 0 3px 1px -2px rgba(0, 0, 0, 0.2);
        }
        
        .upload {
          height: 64px;
          width: 64px;
        }
        
        .empty {
        height: 0;
        width: 0;
        }
        
        
      </style>

      <div class="card">
        <vaadin-upload target="serverUrl" method="POST" timeout="300000" headers="{'X-Custom-Header': 'value'}" form-data-name="my-attachment">
          <iron-icon class="upload" slot="add-button" icon="my-icons:file-upload"></iron-icon>
          <div slot="drop-label-icon" class="empty"></div>
          <div slot="drop-label" class="empty"></div>
        </vaadin-upload>
      </div>
      
    `;
  }
}

window.customElements.define('my-view1', MyView1);
