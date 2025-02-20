# Declare characters with unique colors and names.
define u = Character("User", color="#C8FFC8")
define ubuntu = Character("Ubuntu", color="#0099FF")
define fedora = Character("Fedora", color="#FF6600")
define arch = Character("Arch", color="#888888")
define debian = Character("Debian", color="#FFCC00")
define mint = Character("Mint", color="#33CC33")

# Time management
default current_day = 1
default max_days = 7
default time_of_day = "morning"
default energy = 3

# Initialize relationship stats for each distro.
default stats = {
    "ubuntu": {"intimacy": 0, "shared": 0, "risk": 0, "innovation": 0},
    "fedora": {"intimacy": 0, "shared": 0, "risk": 0, "innovation": 0},
    "arch": {"intimacy": 0, "shared": 0, "risk": 0, "innovation": 0},
    "debian": {"intimacy": 0, "shared": 0, "risk": 0, "innovation": 0},
    "mint": {"intimacy": 0, "shared": 0, "risk": 0, "innovation": 0},
}

# Weights for compatibility calculation.
default w_intimacy = 1.0
default w_shared = 1.0
default w_risk = 1.0
default w_innovation = 0.8

# Function to update compatibility score.
init python:
    def calc_compatibility(name):
        s = stats[name]
        return (w_intimacy * s["intimacy"] + 
                w_shared * s["shared"] - 
                w_risk * s["risk"] + 
                w_innovation * s["innovation"])
    
    def advance_time():
        global time_of_day, current_day, energy
        if time_of_day == "morning":
            time_of_day = "afternoon"
        elif time_of_day == "afternoon":
            time_of_day = "evening"
        else:
            time_of_day = "morning"
            current_day += 1
            energy = 3

# Background definitions
image bg terminal_festival = im.Scale("images/backgrounds/terminal_festival.webp", 1920, 1080)
image bg ubuntu_pavilion = im.Scale("images/backgrounds/ubuntu_pavilion.webp", 1920, 1080)
image bg fedora_lounge = im.Scale("images/backgrounds/fedora_lounge.webp", 1920, 1080)
image bg arch_hub = im.Scale("images/backgrounds/arch_hub.webp", 1920, 1080)
image bg debian_center = im.Scale("images/backgrounds/debian_center.webp", 1920, 1080)
image bg mint_cafe = im.Scale("images/backgrounds/mint_cafe.webp", 1920, 1080)

transform fullscreen:
    size (1920, 1080)
    xalign 0.5
    yalign 0.5

# Main start label.
label start:
    show bg terminal_festival at fullscreen
    u "Welcome to the Festival of Free Software! [current_day] days of open-source romance await..."
    
    call screen show_distro_profiles
    
    while current_day <= max_days and energy > 0:
        call daily_schedule
    
    jump ending

label daily_schedule:
    $ location_choices = []
    if energy > 0:
        menu:
            "Where would you like to go? ([energy] energy remaining)"
            "Visit Ubuntu's Pavilion":
                $ energy -= 1
                jump ubuntu_date
            "Head to Fedora's Experimental Lounge":
                $ energy -= 1
                jump fedora_date
            "Explore Arch's Minimalist Hub":
                $ energy -= 1
                jump arch_date
            "Stop by Debian's Stable Center":
                $ energy -= 1
                jump debian_date
            "Swing by Mint's Sleek Cafe":
                $ energy -= 1
                jump mint_date
            "Rest and recover energy":
                $ energy = 3
                $ advance_time()
    return

# Sample branch for Ubuntu date.
label ubuntu_date:
    show bg ubuntu_pavilion at fullscreen
    show ubuntu neutral at center
    ubuntu "Welcome, User! I'm Ubuntu—here to help you navigate life's commands with a friendly smile."
    
    menu:
        "How do you respond?"
        
        "Ask for a system update on her mood":
            show ubuntu happy
            ubuntu "I'm running smoothly today, thank you for asking!"
            $ stats["ubuntu"]["intimacy"] += 1
            
        "Compliment her user-friendliness":
            show ubuntu blushing
            ubuntu "That's so sweet! I do try to be approachable."
            $ stats["ubuntu"]["intimacy"] += 2
            $ stats["ubuntu"]["shared"] += 1
            
        "Throw a risky command that might break the system":
            show ubuntu worried
            ubuntu "Hey now, let's not do anything rash..."
            $ stats["ubuntu"]["risk"] += 2
            $ stats["ubuntu"]["intimacy"] -= 1
    
    $ comp = calc_compatibility("ubuntu")
    if comp >= 5:
        jump ubuntu_good_ending
    elif comp >= 2:
        jump ubuntu_neutral_ending
    else:
        jump ubuntu_bad_ending

label ubuntu_good_ending:
    scene bg ubuntu_pavilion
    show cg ubuntu_romantic
    with fade
    
    ubuntu "It looks like our commands are perfectly in sync. I think this could be the start of a beautiful open-source partnership!"
    
    hide cg ubuntu_romantic
    show ubuntu happy at center
    
    u "I'm glad we updated our connection."
    
    show cg ubuntu_ending
    with fade
    
    ubuntu "Let's compile our future together!"
    
    return

label ubuntu_neutral_ending:
    ubuntu "We might need to tweak some configurations, but there's definitely potential here."
    u "Let's try to debug our issues and reconnect later."
    return

label ubuntu_bad_ending:
    ubuntu "I'm sorry, but your commands are causing too many errors. Maybe it's best we don't merge."
    u "I understand…"
    return

label fedora_date:
    show bg fedora_lounge at fullscreen
    show fedora neutral at center
    
    if time_of_day == "morning":
        show fedora excited
        fedora "Good morning! Want to help me test this experimental new package?"
        menu:
            "How do you respond?"
            "Eagerly volunteer to help":
                $ stats["fedora"]["innovation"] += 2
                $ stats["fedora"]["intimacy"] += 1
                show fedora happy
                fedora "That's the spirit! Innovation is in our DNA!"
            "Ask about safety precautions first":
                $ stats["fedora"]["shared"] += 1
                $ stats["fedora"]["risk"] -= 1
                show fedora thinking
                fedora "Smart thinking. We're bold, but not reckless!"
            "Suggest improving documentation instead":
                $ stats["fedora"]["shared"] += 2
                fedora "Documentation is crucial for community growth!"
    
    elif time_of_day == "afternoon":
        fedora "Perfect timing! I'm working on some bleeding-edge features."
        menu:
            "How do you engage?"
            "Offer to contribute code":
                $ stats["fedora"]["innovation"] += 3
                $ stats["fedora"]["intimacy"] += 2
                fedora "Wow, you really get me! Let's innovate together!"
            "Share user feedback":
                $ stats["fedora"]["shared"] += 2
                fedora "User perspective is invaluable for development!"
            "Warn about potential stability issues":
                $ stats["fedora"]["risk"] -= 1
                fedora "Sometimes we need to take calculated risks..."
    
    else:  # evening
        fedora "Evening! Care to join me for some kernel compilation and chill?"
        menu:
            "Your response?"
            "Absolutely!":
                $ stats["fedora"]["intimacy"] += 3
                $ stats["fedora"]["innovation"] += 1
                fedora "You're really something special..."
            "Maybe something less intense?":
                $ stats["fedora"]["shared"] += 1
                fedora "We can start with something simpler."
            "That sounds dangerous":
                $ stats["fedora"]["risk"] += 1
                fedora "Living on the edge is part of the fun!"

    $ advance_time()
    $ comp = calc_compatibility("fedora")
    if comp >= 8:
        jump fedora_good_ending
    elif comp >= 4:
        jump fedora_neutral_ending
    else:
        jump fedora_bad_ending

label fedora_good_ending:
    fedora "Our collaboration has been revolutionary! Let's keep pushing boundaries together!"
    u "With you, every update feels like an adventure."
    return

label fedora_neutral_ending:
    fedora "We've made some interesting discoveries. Maybe we can innovate more next time?"
    u "I'll study up on the latest tech trends."
    return

label fedora_bad_ending:
    fedora "I need someone who can keep up with rapid development cycles..."
    u "I guess I'm more stable-release material."
    return

label arch_date:
    show bg arch_hub at fullscreen
    show arch neutral at center
    
    if time_of_day == "morning":
        show arch thinking
        arch "I see you've found your way here without hand-holding. Impressive."
        menu:
            "How do you approach Arch?"
            "Show off your custom kernel compilation":
                $ stats["arch"]["innovation"] += 2
                $ stats["arch"]["intimacy"] += 2
                show arch happy
                arch "Finally, someone who understands the importance of building from source."
            "Mention you read the entire wiki":
                $ stats["arch"]["shared"] += 3
                arch "RTFM - music to my ears."
            "Ask for help with installation":
                $ stats["arch"]["risk"] += 1
                $ stats["arch"]["intimacy"] -= 1
                arch "The wiki exists for a reason..."
    
    elif time_of_day == "afternoon":
        arch "Care to join me in optimizing some makeflags?"
        menu:
            "Your response?"
            "Suggest parallel compilation techniques":
                $ stats["arch"]["innovation"] += 3
                $ stats["arch"]["shared"] += 1
                arch "Your understanding of system resources is... adequate."
            "Share your custom PKGBUILDs":
                $ stats["arch"]["shared"] += 2
                $ stats["arch"]["intimacy"] += 1
                arch "These are elegantly minimal. We should collaborate."
            "Prefer using pre-built binaries":
                $ stats["arch"]["risk"] -= 1
                $ stats["arch"]["innovation"] -= 1
                arch "How... conventional."
    
    else:  # evening
        arch "I'm reviewing some AUR packages. You may observe."
        menu:
            "What do you do?"
            "Audit the PKGBUILD scripts together":
                $ stats["arch"]["intimacy"] += 3
                $ stats["arch"]["shared"] += 2
                arch "Your attention to security is... commendable."
            "Propose improvements to the build process":
                $ stats["arch"]["innovation"] += 2
                $ stats["arch"]["shared"] += 1
                arch "Interesting optimization strategy."
            "Install without checking the PKGBUILD":
                $ stats["arch"]["risk"] += 3
                arch "That's dangerously irresponsible."

    $ advance_time()
    $ comp = calc_compatibility("arch")
    if comp >= 8:
        jump arch_good_ending
    elif comp >= 4:
        jump arch_neutral_ending
    else:
        jump arch_bad_ending

label arch_good_ending:
    arch "Your technical prowess and commitment to minimalism align perfectly with my philosophy."
    u "Together, we'll keep our systems clean and efficient."
    return

label arch_neutral_ending:
    arch "You show potential, but need more experience with advanced system administration."
    u "I'll keep studying the wiki and practicing."
    return

label arch_bad_ending:
    arch "This isn't going to work. You clearly prefer systems that hold your hand."
    u "Maybe I should stick to more user-friendly distros..."
    return

label debian_date:
    show bg debian_center at fullscreen
    show debian neutral at center
    
    if time_of_day == "morning":
        show debian happy
        debian "Welcome to the Stable Center. We believe in thorough testing and reliability."
        menu:
            "How do you respond?"
            "Share your experience with long-term support releases":
                $ stats["debian"]["shared"] += 3
                $ stats["debian"]["intimacy"] += 1
                debian "It's refreshing to meet someone who values stability."
            "Discuss security vulnerability management":
                $ stats["debian"]["innovation"] += 1
                $ stats["debian"]["shared"] += 2
                debian "Security is indeed our top priority."
            "Suggest using testing/unstable branches":
                $ stats["debian"]["risk"] += 2
                debian "That's... not our recommended approach."
    
    elif time_of_day == "afternoon":
        debian "I'm reviewing some package maintenance policies. Would you like to join?"
        menu:
            "What's your approach?"
            "Offer to help with QA testing":
                $ stats["debian"]["shared"] += 2
                $ stats["debian"]["intimacy"] += 2
                debian "Your commitment to quality is admirable."
            "Propose policy improvements":
                $ stats["debian"]["innovation"] += 2
                $ stats["debian"]["shared"] += 1
                debian "Interesting suggestions, we'll need to discuss these in detail."
            "Rush through the review":
                $ stats["debian"]["risk"] += 2
                $ stats["debian"]["shared"] -= 1
                debian "We prefer thorough consideration over hasty decisions."
    
    else:  # evening
        debian "Care to discuss our social contract over some tea?"
        menu:
            "Your response?"
            "Express dedication to free software principles":
                $ stats["debian"]["shared"] += 3
                $ stats["debian"]["intimacy"] += 2
                debian "Your values align perfectly with ours."
            "Share ideas about community governance":
                $ stats["debian"]["innovation"] += 1
                $ stats["debian"]["shared"] += 2
                debian "These are thoughtful perspectives on our democratic process."
            "Suggest more corporate involvement":
                $ stats["debian"]["risk"] += 1
                $ stats["debian"]["shared"] -= 1
                debian "Our community values independence above all."

    $ advance_time()
    $ comp = calc_compatibility("debian")
    if comp >= 8:
        jump debian_good_ending
    elif comp >= 4:
        jump debian_neutral_ending
    else:
        jump debian_bad_ending

label debian_good_ending:
    debian "Your commitment to stability and free software principles shows great promise for a long-term partnership."
    u "I believe in building something that lasts."
    return

label debian_neutral_ending:
    debian "You understand our values, but there's still much to learn about our processes."
    u "I appreciate the thorough approach to everything."
    return

label debian_bad_ending:
    debian "I don't think you fully appreciate the importance of stability and careful consideration."
    u "Perhaps I'm too focused on quick results..."
    return

label mint_date:
    show bg mint_cafe at fullscreen
    show mint neutral at center
    
    if time_of_day == "morning":
        show mint happy
        mint "Welcome to our cozy cafe! Would you like to try our signature Cinnamon blend?"
        menu:
            "How do you respond?"
            "Appreciate the polished desktop environment":
                $ stats["mint"]["shared"] += 2
                $ stats["mint"]["intimacy"] += 2
                mint "I'm glad you notice the attention we put into the user experience!"
            "Suggest UI/UX improvements":
                $ stats["mint"]["innovation"] += 2
                $ stats["mint"]["shared"] += 1
                mint "That's a creative way to make things even more intuitive!"
            "Complain about default settings":
                $ stats["mint"]["risk"] += 1
                $ stats["mint"]["shared"] -= 1
                mint "We carefully choose defaults to suit most users..."
    
    elif time_of_day == "afternoon":
        mint "I'm working on making some system tools more accessible. Want to help?"
        menu:
            "Your approach?"
            "Offer user feedback and testing":
                $ stats["mint"]["shared"] += 3
                $ stats["mint"]["intimacy"] += 1
                mint "User perspective is exactly what we need!"
            "Propose new user-friendly features":
                $ stats["mint"]["innovation"] += 2
                $ stats["mint"]["shared"] += 2
                mint "These ideas could really help new users feel at home."
            "Suggest removing 'unnecessary' safety features":
                $ stats["mint"]["risk"] += 2
                mint "We believe in keeping our users safe and comfortable."
    
    else:  # evening
        mint "Care to join me for some update management and relaxation?"
        menu:
            "Your response?"
            "Help test update stability":
                $ stats["mint"]["shared"] += 2
                $ stats["mint"]["intimacy"] += 2
                mint "Your dedication to system reliability is wonderful!"
            "Share ideas for smoother updates":
                $ stats["mint"]["innovation"] += 2
                $ stats["mint"]["shared"] += 1
                mint "That could make the process even more seamless."
            "Push untested updates":
                $ stats["mint"]["risk"] += 3
                mint "That's not how we do things here..."

    $ advance_time()
    $ comp = calc_compatibility("mint")
    if comp >= 8:
        jump mint_good_ending
    elif comp >= 4:
        jump mint_neutral_ending
    else:
        jump mint_bad_ending

label mint_good_ending:
    mint "Your understanding of user-friendly design and system stability makes you perfect for me!"
    u "Together, we'll make computing accessible and enjoyable for everyone."
    return

label mint_neutral_ending:
    mint "You have good ideas about user experience, but we need to align more on implementation."
    u "I'll focus more on balancing innovation with reliability."
    return

label mint_bad_ending:
    mint "I need someone who truly understands the importance of user comfort and system stability."
    u "I guess I should work on being more user-focused..."
    return

label ending:
    # Calculate final compatibility scores
    python:
        final_scores = {}
        for distro in stats:
            final_scores[distro] = calc_compatibility(distro)
        best_match = max(final_scores, key=final_scores.get)
    
    if best_match == "ubuntu":
        jump ubuntu_good_ending
    elif best_match == "fedora":
        jump fedora_good_ending
    elif best_match == "arch":
        jump arch_good_ending
    elif best_match == "debian":
        jump debian_good_ending
    else:
        jump mint_good_ending

# Screen to show distro profiles (could later be expanded to include images, voiceovers, etc.)
screen show_distro_profiles:
    tag menu
    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            text "Meet the Distros:"
            text "Ubuntu - Warm, supportive, user-friendly."
            text "Fedora - Bold, innovative, experimental."
            text "Arch - Minimalist, challenging, precise."
            text "Debian - Stable, wise, time-tested."
            text "Mint - Elegant, refined, straightforward."
    timer 5.0 action Return()

