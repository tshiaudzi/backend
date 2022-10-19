// alert("JS is here")
// create function
const navSlide = function(){
    // select burger div and nav div from the DOM
    const burger = document.querySelector(".burger");
    const nav = document.querySelector(".nav-links");
    // select all the links
    const navLinks = nav.querySelectorAll(".nav-links li");

    //Toggle navigation
    burger.addEventListener('click', function(){
        nav.classList.toggle("nav-active");

        navLinks.forEach((link, index) => {
            // console.log(link, index);
            if(link.style.animation === true){
                link.style.animation = '';
            } else{
                // Animate links
                link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 0.2}s`
            }
        });
        
        // burger Animation
        burger.classList.toggle("toggle")
    })

}
navSlide()

// PRODUCT FILTER SECTION START //
const btns = document.querySelectorAll(".btn");
// console.log(btns)
const blogItems = document.querySelectorAll('.card-items');
// console.log(blogItems)

for(let i = 0; i < btns.length; i++){
    btns[i].addEventListener('click', function(e){
        e.preventDefault()
        const filter = e.target.dataset.filter


        // create foreach loop
        blogItems.forEach((blogItem) => {
            if(filter ==='all'){
                blogItem.style.display = 'flex';
            }else{
                if(blogItem.classList.contains(filter)){
                    blogItem.style.display = 'flex';
                }else{
                    blogItem.style.display = 'none';
                }
            }
        })
    })
}

// PRODUCT FILTER SECTION END //
