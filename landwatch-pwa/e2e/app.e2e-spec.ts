import { LandwatchPwaPage } from './app.po';

describe('landwatch-pwa App', function() {
  let page: LandwatchPwaPage;

  beforeEach(() => {
    page = new LandwatchPwaPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
