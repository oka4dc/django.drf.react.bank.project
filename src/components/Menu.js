import React from 'react';
import {
  IonMenu,
  IonContent,
  IonHeader,
  IonToolbar,
  IonTitle,
  IonList,
  IonItem,
  IonLabel
} from '@ionic/react';

export const Menu = () => (
  <IonMenu contentId="main">
    <IonHeader>
      <IonToolbar>
        <IonTitle>Menu</IonTitle>
      </IonToolbar>
    </IonHeader>
    <IonContent>
      <IonList>
        <IonItem button routerLink="/accounts">
          <IonLabel>Accounts</IonLabel>
        </IonItem>
      </IonList>
    </IonContent>
  </IonMenu>
);
