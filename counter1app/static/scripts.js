
const counter = document.getElementById('counter')
let counterval = parseInt(counter.textContent)

let smsSize = 0
const updateTime = 100
const tresh = 300
let counted = false

$.ajax({
    type: 'GET',
    url: '/sms-json/',
    success: function(response){
        smsSize = response.sms_count
        console.log(smsSize)
    },
    console: function(error){
        console.log(error)
    }
})

const runCount = setInterval(()=>{
    console.log('hello world')
    if (counterval < smsSize){
        counterval++
        counter.textContent = counterval 
    }else{
        clearInterval(runCount)
    }
    
}, updateTime)


window.addEventListener('scroll',e=>{
    let position = window.scrollY
    if(position > tresh){
        console.log(position)
    }
    
})