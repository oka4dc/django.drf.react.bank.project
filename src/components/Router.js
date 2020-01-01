import React from 'react';
import { IonReactRouter } from '@ionic/react-router';
import { IonRouterOutlet, IonSplitPane } from '@ionic/react';
import { Route } from 'react-router-dom';

import { LoginPage, AccountPage } from '../pages';
import { Menu } from './Menu';

export const Router = () => (
  <IonReactRouter>
    <IonSplitPane contentId="main">
      <Menu />
      <IonRouterOutlet id="main">
        <Route path="/" component={LoginPage} />
        <Route path="/account" component={AccountPage} />
      </IonRouterOutlet>
    </IonSplitPane>
  </IonReactRouter>
);
