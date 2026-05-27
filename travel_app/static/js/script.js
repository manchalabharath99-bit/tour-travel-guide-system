document.addEventListener("DOMContentLoaded", ()=>{

    // Smooth Button Effect
    const buttons = document.querySelectorAll("button");

    buttons.forEach(button=>{

        button.addEventListener("mouseover", ()=>{

            button.style.boxShadow =
            "0 5px 20px rgba(0,0,0,0.3)";

        });

        button.addEventListener("mouseout", ()=>{

            button.style.boxShadow = "none";

        });

    });

    // Welcome Popup
    console.log("Tour Guide System Loaded");

});