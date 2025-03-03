const puppeteer = require('puppeteer');
const TARGET_URL = "https://assistant-web.streamlit.app/";
const WAKE_UP_BUTTON_TEXT = "Click to wake up";
const PAGE_LOAD_GRACE_PERIOD_MS = 8000;

(async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto(TARGET_URL);
    await page.waitForTimeout(PAGE_LOAD_GRACE_PERIOD_MS);

    const checkForHibernation = async (target) => {
        const [button] = await target.$x(`//button[contains(., '${WAKE_UP_BUTTON_TEXT}')]`);
        if (button) {
            console.log("App hibernating. Attempting to wake up!");
            await button.click();
        }
    }

    await checkForHibernation(page);
    const frames = (await page.frames());
    for (const frame of frames) {
        await checkForHibernation(frame);
    }

    await browser.close();
})();
