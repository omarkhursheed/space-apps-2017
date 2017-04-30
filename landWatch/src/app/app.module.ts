import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { RouterModule, Routes } from '@angular/router';


import { AppComponent } from './app.component';
import { VisualComponent } from './visual/visual.component';
import { NewsComponent } from './news/news.component';
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';
import { EntryComponent } from './entry/entry.component';

var homePath:string;
export var login:boolean=true;
if(login){
  homePath='visual';
}else {
  homePath='welcome';
}

const appRoutes: Routes = [
  { path: 'welcome', component: EntryComponent },
  { path: 'visual', component: VisualComponent },
  { path: 'news', component: NewsComponent },
  // {
  //   path: 'heroes',
  //   component: HeroListComponent,
  //   data: { title: 'Heroes List' }
  // },
  { path: '',
    redirectTo: homePath,
    pathMatch: 'full'
  },
  { path: '**', component: PageNotFoundComponent }
];


@NgModule({
  declarations: [
    AppComponent,
    VisualComponent,
    NewsComponent,
    PageNotFoundComponent,
    EntryComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    RouterModule.forRoot(appRoutes)
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
