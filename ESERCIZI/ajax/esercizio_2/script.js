function getRadioCheckedValue(radioGroup) {
    for (option of radioGroup) {
        if (option.checked) {
            return option.values;
        }
    }
}

function getCheckboxValues(checkBox) {
    var checked = []
    for (option of checkBox) {
        if (option.checked) {
            checked.push(option.value)
        }
    }

    return checked;
}

function getSelectedValues(sel) {
    return sel.options[sel.selectedIndex].value;
}


var form = document.getElementById('regForm');
form.onsubmit = function (event) {
    event.preventDefault(); // Prevent page refresh

    // 1. Create XMLHttpRequest object to do a post request to https://httpbin.org/post
    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'https://httpbin.org/post', true);

    // 2. Set Request header to accept a JSON content
    xhr.setRequestHeader('Content-Type', 'application/json');

    // 3. Get input values to send
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
    var email = document.getElementById('email').value;
    var gender = getRadioCheckedValue(document.getElementsByName('gender'));
    var interests = getCheckboxValues(document.getElementsByName('interests'));
    var country = getCheckboxValues(document.getElementsByName('country'));

    // 4. Convert them to JSON
    var params = JSON.stringify({
        username: username,
        password: password,
        email: email,
        gender: gender,
        interests: interests,
        country: country
    });


    // 5. Create the callback function to get server response
    xhr.onreadystatechange = function () {

        if (xhr.readyState == 4 && xhr.status == 200) {
            var response = JSON.parse(xhr.response);
            var data = JSON.parse(response.data);
            var responseUsername = data.username;

            document.getElementById('response').innerHTML = 'Utente ' + responseUsername + ' creato!';
        } else if (xhr.readyState === 4) {
            document.getElementById('response').innerHTML = 'Errore durante l\'invio dei dati.';
            document.getElementById('response').style.color = 'red';
        }
    }

    // 6. Send params to the server
    xhr.send(params);
};
