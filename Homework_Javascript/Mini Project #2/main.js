const drums = document.getElementsByClassName("empty-square");
const music = document.querySelector('audio');

for(const drum of drums){
    drum.addEventListener('click', ()=> {
        console.log(music)
        music.src = `./sounds/${drum.dataset.name}.wav`;

        music.play();
    })
}
