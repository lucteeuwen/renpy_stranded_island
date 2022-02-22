# Renpy Stranded Island - Game
### :family: Contributers
Chapter1 =  [Shaurya](https://github.com/DHASSWAGGER) <br>
Chapter2 = [Luc](https://github.com/luc-frenkie-dj) <br>
Chapter3 = [Parsa](https://github.com/ParsaThsi) <br>
Extras = [Harel](https://github.com/poo-goblin) <br>

### :floppy_disk: Instalation
1. Download the SDK from the renpy website: https://www.renpy.org/latest.html
2. Clone the git repository inside the renpy SDK using:
```
git clone https://github.com/luc-frenkie-dj/renpy_stranded_island.git
```
3. Run the renpy executable in the SDK and enjoy!

### :blue_book: Things I learnt
- Basic Renpy project structure <br>
    ***This image shows the basic project structure in which all the files are inside of the game folder. Then there are also folders for images, cache and game saves.***
  ![project structure image](http://pm1.narvii.com/7114/b9fb2f5fdee08cbd15c95a6986a32e734f49b78ar1-1061-890v2_uhq.jpg)
    
- Basic Renpy syntax <br>
    ***This code snipped shows basic RenPy syntax in which a label is create, an option is proposed to the user and the character is rendered conditionally***

  ```python
  label Chapter2:
    scene bg island
    if gender == "m":
        show male basic
    elif gender == "f":
        show female basic
    menu:
        "Are you going to panic?":
            jump choice_panic
        "Are you going to cry?":
            jump choice_cry
        "Are you going to start doing some work?":
            jump choice_work
  ```

- Different types of inputs
- Changes of scenes and images
- Changes in the main configuration of the project <br>
       ***This is a code snippet from the project in which some of the configurations can be changed of the project such as name and config version***
    ```python
      # Change project window title
      define config.name = _("Stranded Island")

      # Allow show name in GUI window
      define gui.show_name = True

      # Define game version
      define config.version = "1.0"

    ```

- USing images and using properly sized images

### :books: Things I can teach
- Basic Renpy project structure
- Basic Renpy syntax
- Different types of inputs
- Changes of scenes and images
- Changes in the main configuration of the project
- Using images and using properly sized images
- Python syntax

### :globe_with_meridians: Bibliography / resources
> https://lemmasoft.renai.us/forums/viewtopic.php?f=52&t=17302 <br>
> https://emily2.itch.io/sutemo <br>
> https://stackoverflow.com/ <br>
> Renpy Tutorial Project inside the RenPy launcher <br>
