import React from 'react';
import { IonReactRouter } from '@ionic/react-router';
import { IonRouterOutlet } from '@ionic/react';
import { Route } from 'react-router-dom';

import { LoginPage } from '../pages';

export const Router = () => (
  <IonReactRouter>
    <IonRouterOutlet>
      <Route path="/" component={LoginPage} />
    </IonRouterOutlet>
  </IonReactRouter>
);
