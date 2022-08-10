// records 

var selections=[]
var answers=[];
var answered=false;
var score=0;
var number=0;



//words to review 

var reviews =[]


// triggers 
document.addEventListener("DOMContentLoaded",function(){
    document.querySelectorAll('.level').forEach(selectButton=>{
        selectButton.onclick= select;
    })
    document.querySelector('#start').onclick = start;
    document.querySelectorAll('.next').forEach(nextButton=>
      nextButton.onclick = next); 

    document.querySelectorAll('.answer').forEach(an =>{
      an.onclick=answer});

  });

  
function scoring(){
  const percent = (parseInt(score)/parseInt(number)) *100;
  document.querySelector('#score').innerText= `${percent.toString()} %`;  
  }


function answer(e){
    if (answered == false){
    number++;
    const id = e.target.closest('.quiz_section').getAttribute('id')
    const order = parseInt(id.substr(id.length -1))

    answered = true;

    if (e.target.innerText == answers[order]){
      e.target.innerHTML +=" <i class='bi bi-check-circle'></i>"
      score++;
    }
    else{
      reviews.push([answers[order],e.target.closest('.quiz_section').querySelector('#definition').innerText])
      e.target.innerHTML +=' <i class="bi bi-x-circle"></i>'
      e.target.style.color= 'red'
      e.target.closest('.quiz_section').querySelector('#show_answer').innerText = answers[order];
      e.target.closest('.quiz_section').querySelector('#show_answer').style.color = 'green';
      
    }
    //update the score
    scoring();
    }
  }



function next(e){
  if (answered ==true){
  answered =false;
  const id = e.target.parentElement.nextElementSibling.getAttribute('id');
  if (id == 'ending' && reviews.length>0){
    show('loading');
    fetch('/review',{
      method:'POST',
      body: JSON.stringify({
      reviews:reviews
      }),
      }
  ).then(response=>response.json()).then(result =>
    {console.log(result);
    show(id);})
  }else{
  show(id);
  }
  }
}

function select(e){
   const grade = e.target.getAttribute('id');
   if (selections.includes(grade)==false){
    if (selections.length<=2){
   e.target.innerHTML = "<i class='bi bi-check-circle'>"
   selections.unshift(grade)
    }
   }else{
    const index= selections.indexOf(grade)
    selections.splice(index,1);
    e.target.innerText = `Grade ${grade}`
    
   }
  }
   
function start(){
  if (selections.length>0){
    show('loading');
    fetch('/quiz',{
        method:'POST',
        body: JSON.stringify({
        selections:selections
        }),
        }
    ).then(response=>response.json())
    .then(result =>{
        var count = 0;
        document.querySelectorAll('.quiz_section').forEach(section=>
              { 
                
                const quiz = result[count]

                answers.push(quiz['word'])
                // assign definition and quiz to the each quiz_section
                section.querySelector('#definition').innerText = quiz['definition'];
                section.querySelector('#answer_1').innerText = quiz['quiz'][0];
                section.querySelector('#answer_2').innerText = quiz['quiz'][1];
                section.querySelector('#answer_3').innerText = quiz['quiz'][2];
                section.querySelector('#answer_4').innerText = quiz['quiz'][3];
                count++;
              
        })
        show('quiz_0');
    })
  }
  }



function show(id){
    // remove all at first
    document.querySelector('#intro').style.display='none';
    document.querySelector('#loading').style.display='none';
    document.querySelector('#quiz_0').style.display='none';
    document.querySelector('#quiz_1').style.display='none';
    document.querySelector('#quiz_2').style.display='none';
    document.querySelector('#quiz_3').style.display='none';
    document.querySelector('#quiz_4').style.display='none';
    document.querySelector('#quiz_5').style.display='none';
    document.querySelector('#quiz_6').style.display='none';
    document.querySelector('#quiz_7').style.display='none';
    document.querySelector('#quiz_8').style.display='none';
    document.querySelector('#quiz_9').style.display='none';
    document.querySelector('#ending').style.display='none';

    document.querySelector(`#${id}`).style.display='block';
    
}

  