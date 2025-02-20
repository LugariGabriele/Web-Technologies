const arr = [
    {
        url: "https://www.armandoalpantheon.it/wp-content/uploads/2023/03/Primavera-a-Roma-%E2%80%93-Il-Colosseo-e-gli-scavi-di-Ostia-Antica-armando-al-pantheon-768x480.jpg",
        title: "Colosseo",
        description: "Originariamente conosciuto come Anfiteatro Flavio è il più grande anfiteatro romano del mondo.",
    },
    {
        url: "https://png.pngtree.com/background/20230525/original/pngtree-floral-wallpaper-with-brown-and-brown-paint-picture-image_2735082.jpg",
        title: "Linguaggio dei fiori",
        description: "Modo di comunicazione ottocentesco per cui i fiori e gli allestimenti floreali venivano utilizzati per esprimere sensazioni che non sempre potevano essere pronunciate.",
    },
    {
        url: "https://www.donne.it/wp-content/uploads/2023/10/intelligenza-artificiale-768x512.jpg",
        title: "Intelligenza Artificiale",
        description: "Nel suo significato più ampio, è la capacità di un sistema artificiale di simulare l'intelligenza umana attraverso l'ottimizzazione di funzioni matematiche.",
    },
];


function createCard(data) {
    // div representing a card
    var card = document.createElement("div");
    card.className = "w-full md:w-1/2 xl:w-1/3 px-4";

    // Inner div
    var innerDiv = document.createElement("div");
    innerDiv.className = "bg-white rounded-lg overflow-hidden mb-10 shadow-xl";
    // Append the innerd div to the card div
    card.appendChild(innerDiv);

    var image = document.createElement("img");
    image.src = data.url;
    image.className = "w-full";
    // Append the image to the Inner div
    innerDiv.appendChild(image);

    // Div for the title and the paragraph (text div)
    var textContainer = document.createElement("div");
    textContainer.className = "p-8 sm:p-9 md:p-7 xl:p-9 text-center";
    // Append the image to the Inner div
    innerDiv.appendChild(textContainer);

    var title = document.createElement("h3");
    title.className = "font-semibold text-dark text-xl";
    // The function createTextNode is used to escape special characters ('&', '<', '>') and avoid the browser to interpret the as HTML code
    title.appendChild(document.createTextNode(data.title));
    // Append the title to the text div
    textContainer.appendChild(title);

    var description = document.createElement("p");
    description.className = "text-base text-body-color leading-relaxed mb-7";
    description.appendChild(document.createTextNode(data.description));
    // Append the paragraph to the text div
    textContainer.appendChild(description);

    // Append the created card to the container
    document.getElementById("container").appendChild(card);
}
