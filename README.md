# 🚀 Zain-Ul-Arfeen | Sarcastic Developer | Full-Stack Builder

<div align="center">
  <img src="assets/banner.jpg" alt="Profile Banner" width="100%" style="border-radius: 10px; margin-bottom: 20px;">
  
  <h3>💻 Developer | 🐛 Professional Bug Creator | ☕ Powered by Caffeine & Sarcasm</h3>
  
  <p>
    <a href="https://www.linkedin.com/in/zain-ul-arfeen-sarcastic-developer-7a33b9381/">
      <img src="https://img.shields.io/badge/LinkedIn-%230077B5?logo=linkedin&logoColor=white&style=for-the-badge" alt="LinkedIn">
    </a>
    <a href="https://x.com/sarcastic__dev">
      <img src="https://img.shields.io/badge/Twitter-1DA1F2?logo=twitter&logoColor=white&style=for-the-badge" alt="Twitter/X">
    </a>
    <a href="https://github.com/Sarcasticzain">
      <img src="https://img.shields.io/badge/GitHub-%23181717?logo=github&logoColor=white&style=for-the-badge" alt="GitHub">
    </a>
    <a href="https://youtube.com/@sarcasticdeveloper">
      <img src="https://img.shields.io/badge/YouTube-FF0000?logo=youtube&logoColor=white&style=for-the-badge" alt="YouTube">
    </a>
    <a href="https://discord.gg/Fds2kyGHEF">
      <img src="https://img.shields.io/badge/Discord-5865F2?logo=discord&logoColor=white&style=for-the-badge" alt="Discord">
    </a>
  </p>

  <!-- Download Resume -->
  <a href="resume.pdf" download>
    <img src="https://img.shields.io/badge/📄%20Download%20Resume-0077B5?style=for-the-badge&logoColor=white" alt="Download Resume">
  </a>

  <!-- Visitor Counter -->
  <br><br>
  <img src="https://komarev.com/ghpvc/?username=Sarcasticzain&color=blueviolet&style=flat-square" alt="Profile Views">
</div>

---

## 👨‍💻 About Me

<div align="left">
  <img align="right" src="assets/coding-animation.gif" width="350" alt="Coding Animation">

  Hey! I'm **Zain-Ul-Arfeen**, a passionate **full-stack developer** from Pakistan who believes in writing code that's both functional and fun. While my official title is "developer," my real expertise lies in creating sophisticated bugs and then spending hours debugging them while powered by ☕ caffeine and 🎭 sarcasm.

  ### What I Actually Do
  - 💻 Build **ambitious full-stack web applications** that work (mostly)
  - 🎮 Create **interactive experiences** and web tools
  - 🌐 Develop **innovative solutions** that solve real problems
  - 🔧 Build **browser-based applications** and utilities
  - ⚡ Work on **cutting-edge projects** across web technologies
  - 📚 Create **educational content** and share knowledge through YouTube
  - 🎯 Contribute to **community projects** and help others code better

  ### My Philosophy
  I believe in **practical solutions**, **clean code**, and **learning by building**. Every bug is a feature, and every failed project is just a stepping stone to a bigger one. 

  **"Code today, debug tomorrow, cry the day after."** — Me, probably.

  <br>
</div>

---

## 📊 GitHub Stats & Streaks

<div align="center">

### 🔥 GitHub Streaks
![GitHub Streak](https://github-readme-streak-stats.herokuapp.com/?user=Sarcasticzain&theme=tokyonight&hide_border=true&stroke=00FF00)

### 📈 GitHub Statistics
![GitHub Stats](https://github-readme-stats.vercel.app/api?username=Sarcasticzain&show_icons=true&theme=tokyonight&hide_border=true&count_private=true)

### 🌐 Most Used Languages
![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=Sarcasticzain&theme=tokyonight&hide_border=true&layout=compact&count_private=true)

### 📊 Activity Graph
![Activity Graph](https://github-readme-activity-graph.vercel.app/graph?username=Sarcasticzain&theme=tokyo-night&hide_border=true&area=true)

</div>

---

## 🎮 Play Snake Game (While You're Here!)

> **Pro Tip:** Use Arrow Keys to move • Eat the food 🍎 • Don't hit the walls or yourself! • Press SPACEBAR to pause/resume

<div align="center">

<canvas id="gameCanvas" width="400" height="400" style="border: 3px solid #00ff00; background-color: #000; display: block; margin: 20px auto; cursor: pointer; image-rendering: pixelated;"></canvas>

<div style="text-align: center; color: #00ff00; font-family: 'Courier New', monospace; margin: 10px 0;">
  <b>Score: <span id="gameScore">0</span> | High Score: <span id="gameHighScore">0</span></b>
</div>

<p style="text-align: center; color: #888; font-size: 12px; margin-top: 10px;">
  ⬆️ Arrow Keys to move | SPACEBAR to pause | Click to restart | Built with vanilla JavaScript 🎮
</p>

</div>

<script>
(function() {
  // Wait for DOM to be ready
  function startSnakeGame() {
    const canvas = document.getElementById('gameCanvas');
    if (!canvas) {
      setTimeout(startSnakeGame, 100);
      return;
    }
    
    const ctx = canvas.getContext('2d');
    const scoreEl = document.getElementById('gameScore');
    const highScoreEl = document.getElementById('gameHighScore');
    
    const GRID_SIZE = 20;
    const TILE_COUNT = canvas.width / GRID_SIZE;
    
    let snake = [{x: 10, y: 10}];
    let food = {x: 15, y: 15};
    let dx = 1, dy = 0;
    let nextDx = 1, nextDy = 0;
    let score = 0;
    let gameActive = true;
    let gamePaused = false;
    let gameOver = false;
    
    let highScore = parseInt(localStorage.getItem('snakeGameHighScore')) || 0;
    highScoreEl.textContent = highScore;
    
    function resetGame() {
      snake = [{x: 10, y: 10}];
      food = {x: Math.floor(Math.random() * TILE_COUNT), y: Math.floor(Math.random() * TILE_COUNT)};
      dx = 1;
      dy = 0;
      nextDx = 1;
      nextDy = 0;
      score = 0;
      gameActive = true;
      gameOver = false;
      gamePaused = false;
      scoreEl.textContent = score;
      draw();
      gameLoop();
    }
    
    function generateFood() {
      let newFood;
      let foodOnSnake;
      do {
        foodOnSnake = false;
        newFood = {
          x: Math.floor(Math.random() * TILE_COUNT),
          y: Math.floor(Math.random() * TILE_COUNT)
        };
        for (let segment of snake) {
          if (segment.x === newFood.x && segment.y === newFood.y) {
            foodOnSnake = true;
            break;
          }
        }
      } while (foodOnSnake);
      return newFood;
    }
    
    function draw() {
      // Clear canvas
      ctx.fillStyle = '#000';
      ctx.fillRect(0, 0, canvas.width, canvas.height);
      
      // Draw grid
      ctx.strokeStyle = '#0a0a0a';
      ctx.lineWidth = 0.5;
      for (let i = 0; i <= TILE_COUNT; i++) {
        ctx.beginPath();
        ctx.moveTo(i * GRID_SIZE, 0);
        ctx.lineTo(i * GRID_SIZE, canvas.height);
        ctx.stroke();
        
        ctx.beginPath();
        ctx.moveTo(0, i * GRID_SIZE);
        ctx.lineTo(canvas.width, i * GRID_SIZE);
        ctx.stroke();
      }
      
      // Draw snake
      snake.forEach((segment, idx) => {
        ctx.fillStyle = idx === 0 ? '#00ff00' : '#00aa00';
        ctx.fillRect(
          segment.x * GRID_SIZE + 1,
          segment.y * GRID_SIZE + 1,
          GRID_SIZE - 2,
          GRID_SIZE - 2
        );
      });
      
      // Draw food
      ctx.fillStyle = '#ff6b6b';
      ctx.fillRect(
        food.x * GRID_SIZE + 2,
        food.y * GRID_SIZE + 2,
        GRID_SIZE - 4,
        GRID_SIZE - 4
      );
      
      // Draw pause text
      if (gamePaused && gameActive) {
        ctx.fillStyle = 'rgba(0, 255, 0, 0.5)';
        ctx.font = 'bold 20px Arial';
        ctx.textAlign = 'center';
        ctx.fillText('PAUSED', canvas.width / 2, canvas.height / 2);
        ctx.textAlign = 'left';
      }
      
      // Draw game over
      if (gameOver) {
        ctx.fillStyle = 'rgba(255, 0, 0, 0.7)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = '#fff';
        ctx.font = 'bold 28px Arial';
        ctx.textAlign = 'center';
        ctx.fillText('GAME OVER!', canvas.width / 2, canvas.height / 2 - 20);
        ctx.font = 'bold 16px Arial';
        ctx.fillText('Click to Restart', canvas.width / 2, canvas.height / 2 + 20);
        ctx.textAlign = 'left';
      }
    }
    
    function update() {
      if (!gameActive || gamePaused) return;
      
      dx = nextDx;
      dy = nextDy;
      
      const head = {
        x: snake[0].x + dx,
        y: snake[0].y + dy
      };
      
      // Check wall collision
      if (head.x < 0 || head.x >= TILE_COUNT || head.y < 0 || head.y >= TILE_COUNT) {
        gameActive = false;
        gameOver = true;
        draw();
        return;
      }
      
      // Check self collision
      for (let segment of snake) {
        if (head.x === segment.x && head.y === segment.y) {
          gameActive = false;
          gameOver = true;
          draw();
          return;
        }
      }
      
      snake.unshift(head);
      
      // Check food collision
      if (head.x === food.x && head.y === food.y) {
        score += 10;
        scoreEl.textContent = score;
        if (score > highScore) {
          highScore = score;
          highScoreEl.textContent = highScore;
          localStorage.setItem('snakeGameHighScore', highScore);
        }
        food = generateFood();
      } else {
        snake.pop();
      }
    }
    
    function gameLoop() {
      update();
      draw();
      if (gameActive) {
        setTimeout(gameLoop, 120);
      }
    }
    
    // Keyboard controls
    document.addEventListener('keydown', (e) => {
      if (e.key === ' ') {
        if (gameActive && !gameOver) {
          gamePaused = !gamePaused;
        }
        e.preventDefault();
      }
      
      if (e.key === 'ArrowUp' && dy === 0) {
        nextDx = 0;
        nextDy = -1;
      } else if (e.key === 'ArrowDown' && dy === 0) {
        nextDx = 0;
        nextDy = 1;
      } else if (e.key === 'ArrowLeft' && dx === 0) {
        nextDx = -1;
        nextDy = 0;
      } else if (e.key === 'ArrowRight' && dx === 0) {
        nextDx = 1;
        nextDy = 0;
      }
    });
    
    // Mouse click to restart
    canvas.addEventListener('click', () => {
      if (gameOver) {
        resetGame();
      }
    });
    
    // Start the game
    draw();
    gameLoop();
  }
  
  // Start game when document is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', startSnakeGame);
  } else {
    startSnakeGame();
  }
})();
</script>

---

## 🏆 Competitive Programming & Achievements

<div align="center">
  <table>
    <tr>
      <td align="center">
        <img src="https://img.shields.io/badge/LeetCode-Active-yellow?style=flat-square&logo=leetcode" alt="LeetCode">
        <br><b>LeetCode</b>
      </td>
      <td align="center">
        <img src="https://img.shields.io/badge/CodeChef-Participant-orange?style=flat-square&logo=codechef" alt="CodeChef">
        <br><b>CodeChef</b>
      </td>
      <td align="center">
        <img src="https://img.shields.io/badge/HackerRank-5%20Star-brightgreen?style=flat-square&logo=hackerrank" alt="HackerRank">
        <br><b>HackerRank</b>
      </td>
      <td align="center">
        <img src="https://img.shields.io/badge/GeeksforGeeks-Contributor-blue?style=flat-square&logo=geeksforgeeks" alt="GeeksforGeeks">
        <br><b>GeeksforGeeks</b>
      </td>
    </tr>
  </table>
</div>

---

## 🛠️ Tech Stack

### **Languages**
<div>
  <img src="https://skillicons.dev/icons?i=javascript,typescript,python,html,css,bash" alt="Languages">
</div>

### **Frontend**
<div>
  <img src="https://skillicons.dev/icons?i=react,nextjs,vue,html,css,tailwind" alt="Frontend">
</div>

### **Backend & Databases**
<div>
  <img src="https://skillicons.dev/icons?i=nodejs,express,mongodb,postgres,firebase" alt="Backend">
</div>

### **DevOps & Tools**
<div>
  <img src="https://skillicons.dev/icons?i=git,github,docker,vscode,linux,webpack" alt="DevOps">
</div>

---

## 📦 Featured Projects

### 🌤️ [Whaather v3](https://sarcasticzain.github.io/whaather-v3.html)
**Live Weather Forecasts Web App**
- Real-time weather data with beautiful UI
- No API key required - pure client-side magic
- Responsive design for all devices
- Modern weather visualization
- Built with vanilla JavaScript & CSS

### 🔒 [WebSec PRO v3.0](https://sarcasticzain.github.io/WebSec.html)
**Comprehensive Web Security & Analysis Tool**
- 🔍 **Port Scanner** - Scan open ports on any domain
- 🌐 **WHOIS & Domain Info** - Get detailed domain information
- ⚙️ **Technology Stack Detection** - Identify tech used on websites
- ✅ **Blacklist/Malware DB** - Check security status
- 🍪 **Cookie Deep Dive** - Analyze cookies on any site
- 🖥️ **Site Preview** - Live website preview
- 📡 **Social Media Detection** - Find linked social profiles

### 🎮 [My Games Collection](https://sarcasticzain.github.io/games.html)
**Browser-Based Games Built from Scratch**
- Multiple interactive games (including Snake!)
- Pure JavaScript implementations
- Responsive and mobile-friendly
- Built while avoiding real work 😄

### 🌐 [Personal Portfolio](https://sarcasticzain.github.io/)
**Interactive Developer Portfolio Site**
- Modern dark theme design
- Links to all social profiles
- Embedded YouTube channel
- Direct access to all projects
- Showcases sarcasm & coding skills equally

---

## 💼 Experience

<table>
  <tr>
    <td width="30%"><b>Role</b></td>
    <td width="40%"><b>What I Did</b></td>
    <td width="30%"><b>Status</b></td>
  </tr>
  <tr>
    <td>🛠️ Full-Stack Developer</td>
    <td>Built ambitious web applications & tools</td>
    <td>📍 Pakistan</td>
  </tr>
  <tr>
    <td>🎥 Content Creator</td>
    <td>Educational videos & coding tutorials on YouTube</td>
    <td>🔴 Active</td>
  </tr>
  <tr>
    <td>💬 Community Builder</td>
    <td>Growing Discord & Telegram communities</td>
    <td>🔴 Active</td>
  </tr>
  <tr>
    <td>🚀 Open Source Contributor</td>
    <td>Contributing to various web projects</td>
    <td>🔴 Ongoing</td>
  </tr>
</table>

---

## 🎓 Education & Certifications

- 📚 **Computer Science Student** - Studying & Building Projects
- 🏅 **Self-Taught Developer** - Learning through building real projects
- 📖 **Continuous Learner** - Active in tech communities
- 🎯 **Problem Solver** - Tackling challenges on LeetCode & CodeChef

---

## 📈 Key Metrics

<div align="center">
  <table>
    <tr>
      <td align="center">
        <h3>50+</h3>
        <p>Projects</p>
      </td>
      <td align="center">
        <h3>🔴 Active</h3>
        <p>On GitHub</p>
      </td>
      <td align="center">
        <h3>100%</h3>
        <p>Passion</p>
      </td>
      <td align="center">
        <h3>♾️</h3>
        <p>Bugs Found</p>
      </td>
    </tr>
  </table>
</div>

---

## 📚 Content & Resources

I regularly create content about:
- 🎯 Full-stack web development
- 🚀 Building scalable applications
- 🔧 DevOps and deployment strategies
- 💡 Problem-solving approaches
- 🌍 Open-source contributions
- 🎮 Interactive web experiences

**[Watch on YouTube](https://youtube.com/@sarcasticdeveloper)**

---

## 🌟 Open Source Contributions

Active contributor to various web development projects. Always interested in:
- ⭐ Learning from open source
- 📝 Contributing to projects
- 🚀 Building cool stuff
- 🤝 Helping the community

---

## 🤝 Let's Connect

<div align="center">
  <p>
    <b>Find me on these platforms (where I pretend to be productive):</b>
  </p>

  <a href="https://github.com/Sarcasticzain">
    <img src="https://img.shields.io/badge/GitHub-Follow-181717?logo=github&logoColor=white&style=for-the-badge" alt="GitHub">
  </a>
  <a href="https://www.linkedin.com/in/zain-ul-arfeen-sarcastic-developer-7a33b9381/">
    <img src="https://img.shields.io/badge/LinkedIn-Connect-%230077B5?logo=linkedin&logoColor=white&style=for-the-badge" alt="LinkedIn">
  </a>
  <a href="https://x.com/sarcastic__dev">
    <img src="https://img.shields.io/badge/Twitter-Follow-1DA1F2?logo=twitter&logoColor=white&style=for-the-badge" alt="Twitter/X">
  </a>
  <a href="https://youtube.com/@sarcasticdeveloper">
    <img src="https://img.shields.io/badge/YouTube-Subscribe-FF0000?logo=youtube&logoColor=white&style=for-the-badge" alt="YouTube">
  </a>
  <a href="https://discord.gg/Fds2kyGHEF">
    <img src="https://img.shields.io/badge/Discord-Join-5865F2?logo=discord&logoColor=white&style=for-the-badge" alt="Discord">
  </a>
  <a href="https://www.instagram.com/sarcastic.developer">
    <img src="https://img.shields.io/badge/Instagram-Follow-E4405F?logo=instagram&logoColor=white&style=for-the-badge" alt="Instagram">
  </a>
  <a href="https://t.me/sarcasticdeveloper">
    <img src="https://img.shields.io/badge/Telegram-Channel-0088cc?logo=telegram&logoColor=white&style=for-the-badge" alt="Telegram">
  </a>
  <a href="https://www.facebook.com/share/1EPJehcR6u/?mibextid=wwXIfr">
    <img src="https://img.shields.io/badge/Facebook-Follow-1877F2?logo=facebook&logoColor=white&style=for-the-badge" alt="Facebook">
  </a>

  <br><br>

  **💜 Support My Work:**

  <a href="https://www.patreon.com/Sarcastic_developer?utm_campaign=creatorshare_creator">
    <img src="https://img.shields.io/badge/Patreon-Support%20Me-F96854?logo=patreon&logoColor=white&style=for-the-badge" alt="Patreon">
  </a>

  <br><br>

  <b>⭐ If you find my work valuable, consider starring my repositories!</b>

  <p>
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=16&duration=3000&pause=1000&color=00FF00&center=true&vCenter=true&width=550&lines=Code+today%2C+debug+tomorrow%2C+cry+the+day+after.;Full-stack+developer+powered+by+coffee+%26+sarcasm.;Building+ambitious+projects+one+bug+at+a+time.;Beat+my+snake+game+high+score+if+you+can!;Open+source+enthusiast+from+Pakistan.;Always+learning%2C+always+building." alt="Typing SVG">
  </p>

</div>

---

## 📊 More Analytics

<div align="center">

### 🎯 Repository Activity
[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=Sarcasticzain&repo=sarcasticzain&theme=tokyonight&hide_border=true)](https://github.com/Sarcasticzain)

### 💬 Just For Fun
> "The best way to predict the future is to invent it." — Alan Kay
>
> *My version: "The best way to debug your code is to rewrite it from scratch."* 🎭

</div>

---

<div align="center">
  <p>
    <b>🔗 Check out my full portfolio & projects:</b>
  </p>
  <a href="https://sarcasticzain.github.io/">
    <img src="https://img.shields.io/badge/Visit%20My%20Portfolio-00FF00?style=for-the-badge&logo=github&logoColor=black" alt="Portfolio">
  </a>
  
  <br><br>
  
  <p>
    Made with ❤️ (and a lot of ☕ caffeine) by <strong>Zain-Ul-Arfeen</strong> | Based in 🇵🇰 Pakistan
  </p>
  
  <p>
    <em>"Every expert was once a beginner who just refused to give up... or copied Stack Overflow 😄"</em>
  </p>

  <p>
    Last Updated: 2024 | Keep coding, keep smiling! 🚀
  </p>
</div>

---

**P.S. Did you beat my snake game? Drop your high score in the issues! 🐍🏆**
