
const cheerio = require('cheerio');
const axios = require('axios');
const fs = require('fs');

async function scrapeHTML(url) {
    try {
        const response = await axios.get(url);
        const html = response.data;
        
        // Save to a file or print to console
        fs.writeFileSync('output.html', html);
        console.log("HTML saved to output.html");
        
        return html;
    } catch (error) {
        console.error("Error fetching the page:", error);
        return null;
    }
}

const url = "https://denverpioneers.com/index.aspx";
let siteHTML = scrapeHTML(url).then(html => {
    if (html) {
        // load in all the HTML into cheerio
            console.log("HTML length:", html.length);
            const $ = cheerio.load(html);

            // grab the script and run the script locally
            let myScript = $('h2#h2_scoreboard').siblings('script').text();
            // needed to run script and supress errors
            let window = [];
            let document = {
                addEventListener: function(a1, a2){

                }
            }
            eval(myScript);
            // GAME DATA!!! 
            let games = obj['data'];
    }
});

