// TODO: Implement. See Part 5: API calls.
const API_URL = "http://127.0.0.1:5000";

/**
 * API call: POST request to reset the game.
 * @returns The response JSON.
 */
async function apiReset() {
    var url = API_URL + '/reset';

    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    });

    console.log('API call: /reset');
    var data = await response.json();
    console.log(data);

    return data;
}

/**
 * API call: GET request to get the number of guesses.
 * @returns The response JSON.
 */
async function apiGuesses() {
    var url = API_URL + '/guesses';

    const response = await fetch(url, {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    });

    console.log('API call: /guesses');
    var data = await response.json();
    console.log(data);

    return data;
}

/**
 * API call: POST request to select a card.
 * @param {Number} index The card index.
 * @returns The response JSON.
 */
async function apiSelect(index) {
    // TODO: Implement. See Part 5: API calls.
    var url = API_URL + '/select' + "/" + index;

    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    });

    console.log('API call: /select');
    var data = await response.json();
    console.log(data);

    return data;
}

/**
 * API call: GET request to get a card's information.
 * @param {Number} index The card index.
 * @returns The response JSON.
 */
async function apiCard(index) {
    // TODO: Implement. See Part 5: API calls.

    var url = API_URL + '/card' + "/" + index;

    const response = await fetch(url, {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    });

    console.log('API call: /card');
    var data = await response.json();
    console.log(data);

    return data;
}

/**
 * This function is ran when the webpage first loads.
 */
$(async function () {
    // Assign to each image a function to call when clicked.
    // Specifically: select()
    $("img").each(function (key, value) {
        $(this).click({index: key}, select)
    })

    // Assign to the reset button a function to call when clicked.
    // Specifically: reset()
    $("#button").click(reset);

    // Call reset() to start the game logic.
    reset();
})

/**
 * Selects a card.
 */
async function select(event) {
    var index = event.data.index;
    var data = await apiSelect(index);

    // TODO: Implement. See Part 6: Select logic.

    var data2 = await apiGuesses();
    
    $('#message').text(data.message)
    
    $('#label').text(data2.guesses)

    await updateCards();
}

/**
 * Updates cards.
 */
async function updateCards() {
    $("img").each(async function (index, card) {
        var gif = "../Lab1/images/back.gif";

        // TODO: Implement. See Part 7: Update cards logic.

        var data = await apiCard(index);


        if (data.state.localeCompare("up")== 0){
            gif = "../Lab1/images/" + data.card + ".gif";
        }

        
        $(card).attr("src", gif);
    })
}

/**
 * Resets the game.
 */
async function reset() {
    // TODO: Implement. See Part 8: Update reset logic.
    var data = await apiReset();
    
    var data2 = await apiGuesses();
    

    $("img").each(async function (index, card) {
        var gif = "../Lab1/images/back.gif";
        $(card).attr("src", gif);
    })


    $('#label').text(data2.guesses)
    $('#message').text("Reset success!")
}
