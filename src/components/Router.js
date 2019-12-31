import React from 'react';
import { IonReactRouter } from '@ionic/react-router';
import { IonRouterOutlet, IonMenu, IonSplitPane } from '@ionic/react';
import { Route } from 'react-router-dom';

import { LoginPage } from '../pages';

export const Router = () => (
  <IonReactRouter>
    <IonSplitPane contentId="main">
      <IonMenu />
      <IonRouterOutlet id="main">
        <Route path="/" component={LoginPage} />
      </IonRouterOutlet>
    </IonSplitPane>
  </IonReactRouter>
);
