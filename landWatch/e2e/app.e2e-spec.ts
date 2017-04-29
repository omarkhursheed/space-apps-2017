import { LandWatchPage } from './app.po';

describe('land-watch App', () => {
  let page: LandWatchPage;

  beforeEach(() => {
    page = new LandWatchPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
