$(document).ready(function(){ 
 
    $(".primaryContained").on('click', function(){
    $(".comment").addClass("commentClicked");
  });//end click
  $("textarea").on('keyup.enter', function(){
    $(".comment").addClass("commentClicked");
  });//end keyup
  });//End Function
new Vue({
    el: "#app",
    data:{
       title: 'Add a comment',
      newItem: '',
      item: [],
    },
    methods:{
      addItem  (){
      this.item.push(this.newItem);
        this.newItem = "";
      }
  }
  });

  let likebtn = document.querySelector('#likebtn');
  let dislikebtn = document.querySelector('#dislikebtn');
  let input1 = document.querySelector('#input1');
  let input2 = document.querySelector('#input2');

  likebtn.addEventListener('click',()=>{
      input1.value = parseInt(input1.value) + 1;
      input1.style.color = "#12ff00";
  })
  dislikebtn.addEventListener('click',()=>{
      input2.value = parseInt(input2.value) + 1;
      input2.style.color = "#ff0000";
  })
