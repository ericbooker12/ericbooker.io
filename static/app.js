function getEpisode() {

    let season = Math.floor(Math.random() * 8) + 1
    let episode = Math.floor(Math.random() * 11) + 1

    output = `Season: ${season} Episode: ${episode}`

    document.getElementById("episode_to_watch").innerHTML = output;

}