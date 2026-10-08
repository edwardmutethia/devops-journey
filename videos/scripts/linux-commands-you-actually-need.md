# Linux Commands You Actually Need as a Beginner

**Video Title:** Linux Commands You Actually Need as a Beginner
**Channel:** Tech with Edward
**Target Duration:** 10-12 minutes
**Week:** 1 (Bash Scripting + Sysmon)

---

## COLD OPEN (0:00 - 0:30)

**[VISUAL: Terminal screen recording. You typing commands quickly.]**

**EDWARD (V.O.):**
What's up everyone, Edward here. So I've been learning Linux for the past few weeks as part of my DevOps journey, and one thing I noticed is that most Linux tutorials throw like 50 commands at you and you forget half of them.

**[VISUAL: Cut to you on camera.]**

**EDWARD:**
So today, I'm going to show you the 15 commands I actually use every single day. Not 50. Not 100. Just 15. Let's get into it.

**[VISUAL: Title card — "15 Linux Commands You ACTUALLY Need"]**

---

## INTRO (0:30 - 1:00)

**[VISUAL: You on camera, terminal visible in background.]**

**EDWARD:**
Before we start, quick disclaimer — I'm not a Linux expert. I'm learning this stuff just like you. But these are the commands that have stuck with me because I use them every single day. So if you're a beginner, this is for you. If you're intermediate, maybe you'll pick up a tip or two. Let's go.

---

## SECTION 1: NAVIGATION — "Where Am I?" (1:00 - 3:30)

**[VISUAL: Full screen terminal. You type each command and explain.]**

### Command 1: `pwd` (1:00 - 1:30)

**EDWARD (V.O.):**
First up — `pwd`. This stands for "Print Working Directory." It tells you exactly where you are in the file system.

**[TYPE: `pwd`]**

**EDWARD (V.O.):**
Right now I'm in `/home/edward`. Simple, but essential. Always know where you are before you start running commands.

---

### Command 2: `ls` (1:30 - 2:15)

**EDWARD (V.O.):**
Next — `ls`. This lists everything in your current directory.

**[TYPE: `ls`]**

**EDWARD (V.O.):**
But here's the thing — `ls` alone doesn't show you everything. You want to use `ls -la`.

**[TYPE: `ls -la`]**

**EDWARD (V.O.):**
The `-l` gives you the long format — permissions, owner, size, date. The `-a` shows hidden files. See those files starting with a dot? Those are hidden files. You need to see them.

---

### Command 3: `cd` (2:15 - 3:30)

**EDWARD (V.O.):**
Now — `cd`. Change Directory. This is how you move around.

**[TYPE: `cd Documents`]**

**EDWARD (V.O.):**
I just moved into my Documents folder. Let me check where I am.

**[TYPE: `pwd`]**

**EDWARD (V.O.):**
Now I'm in `/home/edward/Documents`. But what if I want to go back?

**[TYPE: `cd ..`]**

**EDWARD (V.O.):**
`cd ..` goes up one level. And if I want to go back to where I just was?

**[TYPE: `cd -`]**

**EDWARD (V.O.):**
`cd -` takes you back to the previous directory. Super useful. And if you're lost and want to go home?

**[TYPE: `cd ~`]**

**EDWARD (V.O.):**
`cd ~` takes you to your home directory. No matter where you are.

---

## SECTION 2: FILE OPERATIONS — "Do Stuff" (3:30 - 6:00)

**[VISUAL: Full screen terminal.]**

### Command 4: `cp` (3:30 - 4:00)

**EDWARD (V.O.):**
`cp` — Copy. You use this to copy files.

**[TYPE: `cp file.txt file_backup.txt`]**

**EDWARD (V.O.):**
I just copied `file.txt` to `file_backup.txt`. Simple.

---

### Command 5: `mv` (4:00 - 4:30)

**EDWARD (V.O.):**
`mv` — Move. This moves files, but it also renames them.

**[TYPE: `mv old_name.txt new_name.txt`]**

**EDWARD (V.O.):**
I just renamed `old_name.txt` to `new_name.txt`. Same command, two uses.

---

### Command 6: `rm` (4:30 - 5:00)

**EDWARD (V.O.):**
`rm` — Remove. This deletes files.

**[TYPE: `rm file.txt`]**

**EDWARD (V.O.):**
Gone. But here's the warning —

**[VISUAL: Big red text on screen: "BE CAREFUL"]**

**EDWARD (V.O.):**
Never, ever type `rm -rf /` or `rm -rf ~`. That will delete everything on your system. No trash bin. No undo. Gone. I've seen people do this. Don't be that person.

---

### Command 7: `mkdir` (5:00 - 5:30)

**EDWARD (V.O.):**
`mkdir` — Make Directory. Creates a folder.

**[TYPE: `mkdir projects`]**

**EDWARD (V.O.):**
Just made a folder called `projects`. And if I want to create nested folders?

**[TYPE: `mkdir -p projects/2026/january`]**

**EDWARD (V.O.):**
The `-p` flag creates parent directories if they don't exist. One command, three folders.

---

### Command 8: `touch` (5:30 - 6:00)

**EDWARD (V.O.):**
`touch` — Creates an empty file.

**[TYPE: `touch notes.txt`]**

**EDWARD (V.O.):**
Just created `notes.txt`. It's empty, but it exists. You can also use `touch` to update a file's timestamp, but 99% of the time you're using it to create empty files.

---

## SECTION 3: VIEWING FILES — "What's Inside?" (6:00 - 8:00)

**[VISUAL: Full screen terminal.]**

### Command 9: `cat` (6:00 - 6:30)

**EDWARD (V.O.):**
`cat` — Concatenate. This shows you what's inside a file.

**[TYPE: `cat notes.txt`]**

**EDWARD (V.O.):**
It's empty because I just created it. Let me add some text.

**[TYPE: `echo "Hello Linux" > notes.txt`]**

**EDWARD (V.O.):**
Now let's see what's inside.

**[TYPE: `cat notes.txt`]**

**EDWARD (V.O.):**
There it is. `cat` is great for quick peeks at small files.

---

### Command 10: `head` and `tail` (6:30 - 7:15)

**EDWARD (V.O.):**
What if you have a huge file? You don't want to scroll through thousands of lines. That's where `head` and `tail` come in.

**[TYPE: `head /var/log/syslog`]**

**EDWARD (V.O.):**
`head` shows you the first 10 lines. And `tail`?

**[TYPE: `tail /var/log/syslog`]**

**EDWARD (V.O.):**
Shows you the last 10 lines. This is actually super useful for checking logs — which is what I'm learning for DevOps.

---

### Command 11: `nano` (7:15 - 8:00)

**EDWARD (V.O.):**
`nano` — A simple text editor inside your terminal.

**[TYPE: `nano notes.txt`]**

**EDWARD (V.O.):**
This opens nano. You can type, edit, save with `Ctrl+O`, and exit with `Ctrl+X`. It's beginner-friendly. Once you get comfortable, you might switch to `vim`, but nano is where you start.

**[VISUAL: Show yourself typing in nano, saving, and exiting.]**

---

## SECTION 4: SYSTEM INFO — "What's Going On?" (8:00 - 9:30)

**[VISUAL: Full screen terminal.]**

### Command 12: `ps` (8:00 - 8:30)

**EDWARD (V.O.):**
`ps` — Process Status. Shows you what's running on your system.

**[TYPE: `ps aux`]**

**EDWARD (V.O.):**
This shows every process running. The `aux` flags give you detailed output. You'll use this a lot in DevOps to check if services are running.

---

### Command 13: `top` (8:30 - 9:00)

**EDWARD (V.O.):**
`top` — System monitor. This is like Task Manager but in your terminal.

**[TYPE: `top`]**

**EDWARD (V.O.):**
Real-time view of CPU, memory, and processes. Press `q` to quit. This is your go-to when your system feels slow.

---

### Command 14: `df` (9:00 - 9:30)

**EDWARD (V.O.):**
`df` — Disk Free. Shows you how much disk space you have left.

**[TYPE: `df -h`]**

**EDWARD (V.O.):**
The `-h` flag makes it human-readable. See that? I've used 45% of my disk. When this hits 90%, you've got problems.

---

## SECTION 5: THE MOST IMPORTANT COMMAND (9:30 - 10:30)

**[VISUAL: Full screen terminal.]**

### Command 15: `man` (9:30 - 10:30)

**EDWARD (V.O.):**
And finally — the most important command. `man`. This stands for "manual."

**[TYPE: `man ls`]**

**EDWARD (V.O.):**
This opens the manual for `ls`. Every command has a manual. You can scroll with arrow keys, search with `/`, and quit with `q`.

**[VISUAL: Show yourself scrolling through the manual.]**

**EDWARD (V.O.):**
Here's the thing — I don't have all these commands memorized. I use `man` when I forget something. This is how you teach yourself. You don't need to memorize everything. You just need to know that `man` exists.

---

## OUTRO (10:30 - 11:30)

**[VISUAL: You on camera.]**

**EDWARD:**
So those are the 15 Linux commands I actually use every single day. If you're just starting out, practice these. Open your terminal and just play around. Break things. Fix them. That's how you learn.

**[VISUAL: Text on screen — "Next Week: Bash Scripting"]**

**EDWARD:**
Next week, I'm going to show you how to combine these commands into bash scripts. That's where the real power is. So if you want to see that, hit subscribe and the bell so you don't miss it.

**[VISUAL: End screen with subscribe button.]**

**EDWARD:**
Thanks for watching. I'll see you in the next one. Peace.

---

## POST-CREDITS (Optional)

**[VISUAL: Bloopers or extra tips.]**

**EDWARD (V.O.):**
Oh — one more thing. If you want a cheat sheet with all these commands, I'll put a link in the description. Download it, print it, stick it on your wall. That's what I did.

---

## PRODUCTION NOTES

**Recording Setup:**
- Use OBS to record terminal + face cam
- Terminal font size: 18pt+ (needs to be readable)
- Use a dark theme for the terminal (easier on the eyes)

**Thumbnail:**
- Split screen: Terminal on left, you pointing on right
- Text: "15 Linux Commands You ACTUALLY Need"
- Bold, high-contrast colors

**Description:**
```
Linux Commands You Actually Need as a Beginner

In this video, I show you the 15 Linux commands I use every single day as part of my DevOps learning journey. These are the essential commands every beginner should know — no fluff, just what works.

Commands covered:
1. pwd
2. ls
3. cd
4. cp
5. mv
6. rm
7. mkdir
8. touch
9. cat
10. head / tail
11. nano
12. ps
13. top
14. df
15. man

⏱️ Timestamps:
0:00 - Intro
1:00 - Navigation (pwd, ls, cd)
3:30 - File Operations (cp, mv, rm, mkdir, touch)
6:00 - Viewing Files (cat, head, tail, nano)
8:00 - System Info (ps, top, df)
9:30 - The Most Important Command (man)
10:30 - Outro

🔗 Resources:
- [Cheat Sheet Link]
- [My DevOps Roadmap]

#Linux #LinuxCommands #DevOps #TechWithEdward #LearnLinux
```

---

*Script written for Tech with Edward — Week 1 content.*
