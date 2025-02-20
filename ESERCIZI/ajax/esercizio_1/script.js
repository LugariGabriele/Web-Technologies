var button = document.getElementById('button');

button.onclick = function () {

    // 1. Create a new object XMLHttpRequest
    var xhr = new XMLHttpRequest();

    // 2. Specify the request type in the endpoint URL 'https://jsonplaceholder.typicode.com/posts'
    xhr.open("GET", " https://jsonplaceholder.typicode.com/posts", true);

    // 3. Define what to on change of request state
    xhr.onreadystatechange = function () {

        // 4. Define the condition
        if (xhr.readyState === 4 && xhr.status === 200) {

            // 5. Parse JSON content of the request
            var posts = JSON.parse(xhr.responseText);

            // 6. Print the first post on the console
            console.log(posts[0]);

            // 7. Select the post container from the DOM
            var postsContainer= document.getElementById('postsContainer');
            postsContainer.innerHTML='';

            // 8. Iterate over the posts to create the visualization
            for (var post of posts){

                // 9. Create a div for each post
                var postDiv = document.createElement('div');
                postDiv.className = 'post';

                // 10. Create HTML content for each post with concatenated strings
                var postHTML = '<h3>Post' +post.id + ':' +post.title+ '</h3>' + '<p>' + post.body + '</p>';

                // 11. Append the post to the postContainer
                postDiv.innerHTML = postHTML;
            }


        }

    }
    // 12. Send the request to the server
    xhr.send();

};


