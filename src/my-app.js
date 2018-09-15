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
import { setPassiveTouchGestures, setRootPath } from '@polymer/polymer/lib/utils/settings.js';
import '@polymer/app-layout/app-drawer/app-drawer.js';
import '@polymer/app-layout/app-drawer-layout/app-drawer-layout.js';
import '@polymer/app-layout/app-header/app-header.js';
import '@polymer/app-layout/app-header-layout/app-header-layout.js';
import '@polymer/app-layout/app-scroll-effects/app-scroll-effects.js';
import '@polymer/app-layout/app-toolbar/app-toolbar.js';
import '@polymer/app-route/app-location.js';
import '@polymer/app-route/app-route.js';
import '@polymer/iron-pages/iron-pages.js';
import '@polymer/iron-selector/iron-selector.js';
import '@polymer/paper-icon-button/paper-icon-button.js';
import './my-icons.js';

// Gesture events like tap and track generated from touch will not be
// preventable, allowing for better scrolling performance.
setPassiveTouchGestures(true);

// Set Polymer's root path to the same value we passed to our service worker
// in `index.html`.
setRootPath(MyAppGlobals.rootPath);

class MyApp extends PolymerElement {
  static get template() {
    return html`
      <style>
        :host {
          --app-primary-color: #a8ffd3;
          --app-secondary-color: black;

          display: block;
        }


        app-header {
          color: rgba(0,0,0,0.98);
          /*background-color: var(--app-primary-color);*/
          background-image: linear-gradient(30deg, #beffd5, #beffff);
        }

        app-header paper-icon-button {
          --paper-icon-button-ink-color: white;
        }
        
        .logo {
          padding-left: 20px;
        }
        
        .option-holder {
          width: 75px;
          height: 64px;
          padding-right: 6px;
          padding-left: 6px;
          display: inline-block;
          font-size: 16px;
          position: relative;
        }
        
        .option-holder.iron-selected {
          font-weight: bold;
        }
        
        .options {
          position: absolute;
          text-align: center;
          top: 50%; left: 50%;
          transform: translate(-50%,-50%);          
          cursor: pointer;
          margin: 0 auto;
          display: inline-block;
          
        }
        
        .options:hover {
          font-size: 17px;
        }


      </style>

      <app-location route="{{route}}" url-space-regex="^[[rootPath]]">
      </app-location>

      <app-route route="{{route}}" pattern="[[rootPath]]:page" data="{{routeData}}" tail="{{subroute}}">
      </app-route>

      <app-drawer-layout fullbleed="" narrow="{{narrow}}">

        <!-- Main content -->
        <app-header-layout has-scrolling-region="">

          <app-header slot="header" condenses="" reveals="" effects="waterfall" style="box-shadow: 0 0 5px 0 #474747">
            <app-toolbar>
              <div main-title="" class="logo">TrackIT</div>
              <iron-selector selected="{{page}}" attr-for-selected="name">
                <div class="option-holder" name="home"><div class="options" >Home</div></div>
                <div class="option-holder" name="about"><div class="options" >About</div></div>
              </iron-selector>
            </app-toolbar>
          </app-header>

          <iron-pages selected="[[page]]" attr-for-selected="name" role="main">
            <my-view1 name="home"></my-view1>
            <my-view2 name="about"></my-view2>
            <my-view404 name="view404"></my-view404>
          </iron-pages>
        </app-header-layout>
      </app-drawer-layout>
    `;
  }

  static get properties() {
    return {
      page: {
        type: String,
        reflectToAttribute: true,
        observer: '_pageChanged'
      },
      routeData: Object,
      subroute: Object
    };
  }

  static get observers() {
    return [
      '_routePageChanged(routeData.page)'
    ];
  }

  goHome() {
    this.page = 'home';
  }

  goAbout() {
    this.page = 'about';
  }

  _routePageChanged(page) {
     // Show the corresponding page according to the route.
     //
     // If no page was found in the route data, page will be an empty string.
     // Show 'view1' in that case. And if the page doesn't exist, show 'view404'.
    if (!page) {
      this.page = 'home';
    } else if (['home', 'about'].indexOf(page) !== -1) {
      this.page = page;
    } else {
      this.page = 'view404';
    }

  }

  _pageChanged(page) {
    // Import the page component on demand.
    //
    // Note: `polymer build` doesn't like string concatenation in the import
    // statement, so break it up.
      window.history.pushState(null, null, '/' + page);

    switch (page) {
      case 'home':
        import('./my-view1.js');
        break;
      case 'about':
        import('./my-view2.js');
        break;
      case 'view404':
        import('./my-view404.js');
        break;
    }
  }
}

window.customElements.define('my-app', MyApp);
