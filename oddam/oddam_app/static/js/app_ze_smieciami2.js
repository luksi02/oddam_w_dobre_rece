document.addEventListener("DOMContentLoaded", function() {
  /**
   * HomePage - Help section
   */
  class Help {
    constructor($el) {
      this.$el = $el;
      this.$buttonsContainer = $el.querySelector(".help--buttons");
      this.$slidesContainers = $el.querySelectorAll(".help--slides");
      this.currentSlide = this.$buttonsContainer.querySelector(".active").parentElement.dataset.id;
      this.init();
    }

    init() {
      this.events();
    }

    events() {
      /**
       * Slide buttons
       */
      this.$buttonsContainer.addEventListener("click", e => {
        if (e.target.classList.contains("btn")) {
          this.changeSlide(e);
        }
      });

      /**
       * Pagination buttons
       */
      this.$el.addEventListener("click", e => {
        if (e.target.classList.contains("btn") && e.target.parentElement.parentElement.classList.contains("help--slides-pagination")) {
          this.changePage(e);
        }
      });
    }

    changeSlide(e) {
      e.preventDefault();
      const $btn = e.target;

      // Buttons Active class change
      [...this.$buttonsContainer.children].forEach(btn => btn.firstElementChild.classList.remove("active"));
      $btn.classList.add("active");

      // Current slide
      this.currentSlide = $btn.parentElement.dataset.id;

      // Slides active class change
      this.$slidesContainers.forEach(el => {
        el.classList.remove("active");

        if (el.dataset.id === this.currentSlide) {
          el.classList.add("active");
        }
      });
    }

    /**
     * TODO: callback to page change event
     */
    changePage(e) {
      e.preventDefault();
      const page = e.target.dataset.page;

      console.log(page);
    }
  }
  const helpSection = document.querySelector(".help");
  if (helpSection !== null) {
    new Help(helpSection);
  }

  /**
   * Form Select
   */
  class FormSelect {
    constructor($el) {
      this.$el = $el;
      this.options = [...$el.children];
      this.init();
    }

    init() {
      this.createElements();
      this.addEvents();
      this.$el.parentElement.removeChild(this.$el);
    }

    createElements() {
      // Input for value
      this.valueInput = document.createElement("input");
      this.valueInput.type = "text";
      this.valueInput.name = this.$el.name;

      // Dropdown container
      this.dropdown = document.createElement("div");
      this.dropdown.classList.add("dropdown");

      // List container
      this.ul = document.createElement("ul");

      // All list options
      this.options.forEach((el, i) => {
        const li = document.createElement("li");
        li.dataset.value = el.value;
        li.innerText = el.innerText;

        if (i === 0) {
          // First clickable option
          this.current = document.createElement("div");
          this.current.innerText = el.innerText;
          this.dropdown.appendChild(this.current);
          this.valueInput.value = el.value;
          li.classList.add("selected");

          this.console.log("click click") // LG
        }

        this.ul.appendChild(li);
      });

      this.dropdown.appendChild(this.ul);
      this.dropdown.appendChild(this.valueInput);
      this.$el.parentElement.appendChild(this.dropdown);
    }

    addEvents() {
      this.dropdown.addEventListener("click", e => {
        const target = e.target;
        this.dropdown.classList.toggle("selecting");

        // Save new value only when clicked on li
        if (target.tagName === "LI") {
          this.valueInput.value = target.dataset.value;
          this.current.innerText = target.innerText;

          this.console.log("click click") // LG
        }
      });
    }
  }
  document.querySelectorAll(".form-group--dropdown select").forEach(el => {
    new FormSelect(el);
  });

  /**
   * Hide elements when clicked on document
   */
  document.addEventListener("click", function(e) {
    const target = e.target;
    const tagName = target.tagName;

    if (target.classList.contains("dropdown")) return false;

    if (tagName === "LI" && target.parentElement.parentElement.classList.contains("dropdown")) {
      return false;
    }

    if (tagName === "DIV" && target.parentElement.classList.contains("dropdown")) {
      return false;
    }

    document.querySelectorAll(".form-group--dropdown .dropdown").forEach(el => {
      el.classList.remove("selecting");
    });
  });

  /**
   * Switching between form steps
   */
  class FormSteps {
    constructor(form) {
      this.$form = form;
      this.$next = form.querySelectorAll(".next-step");
      this.$prev = form.querySelectorAll(".prev-step");
      this.$step = form.querySelector(".form--steps-counter span");
      this.currentStep = 1;

      this.$stepInstructions = form.querySelectorAll(".form--steps-instructions p");
      const $stepForms = form.querySelectorAll("form > div");
      this.slides = [...this.$stepInstructions, ...$stepForms];

      this.init();
    }

    /**
     * Init all methods
     */
    init() {
      this.events();
      this.updateForm();
    }

    /**
     * All events that are happening in form
     */
    events() {
      // Next step
      this.$next.forEach(btn => {
        btn.addEventListener("click", e => {
          e.preventDefault();
          this.currentStep++;
          if (this.currentStep===2)
          {
            console.log("dupa")
            // LG_injection
            get_that_data()
            //LG_injection
          }
          this.updateForm();
        });
      });

      /** LG */


    // tu jestem 15:17 - nie dziala
      // function get_that_data() {
      //     console.log("inside_get_that_data")
      //     const checkbox = document.querySelectorAll("input[type=checkbox][name=categories]")
      //     // var LG_checkboxes = document.querySelectorAll("input[type=checkbox][name=categories]")
      //     let LG_chosen_ones_checkboxes = []
      //     let LG_chosen_ones_checkboxes_2 = []
      //     console.log("those are checkboxes", checkbox)


// checkboxes.forEach(function(checkbox) {
//   checkbox.addEventListener('change', function() {
//       console.log("12")
//     enabledSettings =
//       Array.from(checkboxes) // Convert checkboxes to an array to use filter and map.
//       .filter(i => i.checked) // Use Array.filter to remove unchecked checkboxes.
//       .map(i => i.value) // Use Array.map to extract only the checkbox values from the array of objects.
//
//     console.log(enabledSettings)
//   })
// });

//           document.addEventListener("DOMContentLoaded", function (event) {
//     var _selector = document.querySelector('input[name=categories]');
//     console.log("cos")
//     _selector.addEventListener('change', function (event) {
//         if (_selector.checked) {
//              console.log("checked")
//         } else {
//             console.log("not")
//         }
//     });
// });

          // let check =  checkbox.addEventListener("change", (e) => {
          //     if (e.target.checked) {
          //         console.log("checked")
          //     } else {
          //         console.log("not")
          //     }
          // });
      // };

         // LG_checkboxes.forEach(function(checkbox) {
         //   console.log("for_each")
         //   checkbox.addEventListener('change', function() {
         //     LG_chosen_ones_checkboxes =
         //         Array.from(LG_checkboxes)
         //             .filter(i => i.checked)
         //             console.log("chcecked")
         //             .map(i => i.value)   // tutej moze zmnienbic value na cos innego
         //     console.log(LG_chosen_ones_checkboxes, " also_something")
         //   })
         // })

          // 2 try - dzialo do for each
           // LG_checkboxes.forEach(function(checkbox) {
           // console.log("for_each")
           // LG_checkboxes.addEventListener('change', (e) => {
           //     if(e.target.checked) {
           //         console.log("checbox is checked")
           //         LG_chosen_ones_checkboxes_2.push(checkbox)
           //         console.log(LG_chosen_ones_checkboxes_2)
           //         console.log(" also_something");
           //     } else {
           //         console.log("not checked")
           //     }


            function checkboxFunction() {
  var checkBox = document.querySelectorAll("input[type=checkbox][name=categories]");
  // If the checkbox is checked, display the output text
  if (checkBox.checked == true){
    // text.style.display = "block";
      console.log("checked")
  } else {
    // text.style.display = "none";
      console.log("not checked")
  }
}


                 // Array.from(LG_checkboxes)
                 //     .filter(i => i.checked)
                 //     console.log("chcecked")
                 //     .map(i => i.value)   // tutej moze zmnienbic value na cos innego

      //      })
      //    })
      // }
      // const LG_button = document.querySelector("button")


      /** LG */

      // Previous step
      this.$prev.forEach(btn => {
        btn.addEventListener("click", e => {
          e.preventDefault();
          this.currentStep--;
          this.updateForm();
        });
      });

      // Form submit
      this.$form.querySelector("form").addEventListener("submit", e => this.submit(e));
    }

    /**
     * Update form front-end
     * Show next or previous section etc.
     */
    updateForm() {
      this.$step.innerText = this.currentStep;

      // TODO: Validation

      this.slides.forEach(slide => {
        slide.classList.remove("active");

        if (slide.dataset.step == this.currentStep) {
          slide.classList.add("active");
        }
      });

      this.$stepInstructions[0].parentElement.parentElement.hidden = this.currentStep >= 6;
      this.$step.parentElement.hidden = this.currentStep >= 6;

      // TODO: get data from inputs and show them in summary
    }

    /**
     * Submit form
     *
     * TODO: validation, send data to server
     */
    submit(e) {
      e.preventDefault();
      this.currentStep++;
      this.updateForm();
    }
  }
  const form = document.querySelector(".form--steps");
  if (form !== null) {
    new FormSteps(form);
  }
});
