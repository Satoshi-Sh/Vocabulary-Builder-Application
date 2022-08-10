// triggers 
document.addEventListener("DOMContentLoaded",function(){
    show('#page_1')
    document.querySelectorAll('.reviewed').forEach(reviewedButton=>{
      reviewedButton.onclick=reviewed;})

    document.querySelectorAll('.load').forEach(loadButton=>{
        loadButton.onclick=load
    })
  });

function load(e){
    console.log('cliked')
    const text = e.target.closest('.page').getAttribute('id')
    const page = parseInt(text.split('_')[1]) +1
    const id = '#page_' + page.toString()
    e.target.parentElement.remove()
    show(id)

}

function reviewed(e){
    const card = e.target.closest('.card');
    const word = card.querySelector('.card-title').innerText
    console.log(card)
    fetch('/archive',{
        method:'POST',
        body: JSON.stringify({
        word: word
        }),
        }
    ).then(response=>response.json()).then(result =>
      {console.log(result);
    card.style.animationPlayState='running';
    card.addEventListener('animationend',() => {
        card.remove();
    });
})
}

function show(id){
    const section = document.querySelector(id)
    section.style.display='block';
}