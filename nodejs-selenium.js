const { By, Key, Builder } = require("selenium-webdriver");
require("chromedriver");

function sleepFor(sleepDuration) {
    var now = new Date().getTime();
    while (new Date().getTime() < now + sleepDuration * 1000) { }
}

var username = ""
var password = ""
var twit = ("")

async function selenium() {
    let driver = await new Builder().forBrowser("chrome").build();

    await driver.get("https://twitter.com/login");

    sleepFor(3);
    await driver.findElement(By.xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')).sendKeys(username, Key.RETURN);
    await driver.findElement(By.xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')).sendKeys(password, Key.RETURN);
    sleepFor(6);
    await driver.findElement(By.xpath('//*[@id="react-root"]/div/div[2]/div[1]/div/div/div/div')).click()
    await driver.findElement(By.xpath('//*[@id="react-root"]/div/div/div[2]/div/div/div/div/span')).sendKeys(twit)
    await driver.findElement(By.xpath('//*[@id="react-root"]/div/div[2]/main/div[3]/div/span/span')).click()
}
selenium()
/* , Key.CONTROL + "v" */
