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
<canvas id="snakeCanvas" width="400" height="400" style="border: 3px solid #00ff00; background-color: #000; display: block; margin: 20px auto; cursor: pointer;"></canvas>
<div style="text-align: center; color: #00ff00; font-family: monospace; margin: 10px 0;">
  <b>Score: <span id="score">0</span> | High Score: <span id="highScore">0</span></b>
</div>
<p style="text-align: center; color: #888; font-size: 12px; margin-top: 10px;">
  This game is embedded in your README! Built with vanilla JavaScript 🎮
</p>
</div>

<script>
// Snake Game - Pure JavaScript
(function() {
  const canvas = document.getElementById('snakeCanvas');
  const ctx = canvas.getContext('2d');
  const scoreDisplay = document.getElementById('score');
  const highScoreDisplay = document.getElementById('highScore');
  
  const gridSize = 20;
  const tileCount = canvas.width / gridSize;
  
  let snake = [{x: 10, y: 10}];
  let food = {x: 15, y: 15};
  let direction = {x: 1, y: 0};
  let nextDirection = {x: 1, y: 0};
  let score = 0;
  let highScore = localStorage.getItem('snakeHighScore') || 0;
  let gameRunning = true;
  let gamePaused = false;
  
  highScoreDisplay.textContent = highScore;
  
  // Controls
  document.addEventListener('keydown', (e) => {
    if (e.key === ' ') {
      gamePaused = !gamePaused;
      e.preventDefault();
    }
    
    const key = e.key;
    if (key === 'ArrowUp' && direction.y === 0) nextDirection = {x: 0, y: -1};
    if (key === 'ArrowDown' && direction.y === 0) nextDirection = {x: 0, y: 1};
    if (key === 'ArrowLeft' && direction.x === 0) nextDirection = {x: -1, y: 0};
    if (key === 'ArrowRight' && direction.x === 0) nextDirection = {x: 1, y: 0};
  });
  
  canvas.addEventListener('click', () => {
    if (!gameRunning) {
      snake = [{x: 10, y: 10}];
      direction = {x: 1, y: 0};
      nextDirection = {x: 1, y: 0};
      score = 0;
      scoreDisplay.textContent = score;
      gameRunning = true;
      gamePaused = false;
      update();
    }
  });
  
  function update() {
    if (!gameRunning || gamePaused) {
      setTimeout(update, 100);
      return;
    }
    
    direction = nextDirection;
    const head = {x: snake[0].x + direction.x, y: snake[0].y + direction.y};
    
    // Check walls
    if (head.x < 0 || head.x >= tileCount || head.y < 0 || head.y >= tileCount) {
      gameRunning = false;
      ctx.fillStyle = '#ff0000';
      ctx.font = 'bold 24px Arial';
      ctx.fillText('GAME OVER!', canvas.width/2 - 80, canvas.height/2);
      ctx.font = '16px Arial';
      ctx.fillText('Click to restart', canvas.width/2 - 60, canvas.height/2 + 30);
      return;
    }
    
    // Check self collision
    if (snake.some(segment => segment.x === head.x && segment.y === head.y)) {
      gameRunning = false;
      ctx.fillStyle = '#ff0000';
      ctx.font = 'bold 24px Arial';
      ctx.fillText('GAME OVER!', canvas.width/2 - 80, canvas.height/2);
      ctx.font = '16px Arial';
      ctx.fillText('Click to restart', canvas.width/2 - 60, canvas.height/2 + 30);
      return;
    }
    
    snake.unshift(head);
    
    // Check food
    if (head.x === food.x && head.y === food.y) {
      score += 10;
      scoreDisplay.textContent = score;
      if (score > highScore) {
        highScore = score;
        highScoreDisplay.textContent = highScore;
        localStorage.setItem('snakeHighScore', highScore);
      }
      food = {x: Math.floor(Math.random() * tileCount), y: Math.floor(Math.random() * tileCount)};
    } else {
      snake.pop();
    }
    
    draw();
    setTimeout(update, 100);
  }
  
  function draw() {
    // Clear canvas
    ctx.fillStyle = '#000';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    
    // Draw snake
    ctx.fillStyle = '#00ff00';
    snake.forEach((segment, index) => {
      if (index === 0) ctx.fillStyle = '#00ff00';
      else ctx.fillStyle = '#00aa00';
      ctx.fillRect(segment.x * gridSize + 1, segment.y * gridSize + 1, gridSize - 2, gridSize - 2);
    });
    
    // Draw food
    ctx.fillStyle = '#ff6b6b';
    ctx.fillRect(food.x * gridSize + 1, food.y * gridSize + 1, gridSize - 2, gridSize - 2);
    
    // Draw grid
    ctx.strokeStyle = '#111';
    ctx.lineWidth = 0.5;
    for (let i = 0; i <= tileCount; i++) {
      ctx.beginPath();
      ctx.moveTo(i * gridSize, 0);
      ctx.lineTo(i * gridSize, canvas.height);
      ctx.stroke();
      
      ctx.beginPath();
      ctx.moveTo(0, i * gridSize);
      ctx.lineTo(canvas.width, i * gridSize);
      ctx.stroke();
    }
    
    // Pause indicator
    if (gamePaused) {
      ctx.fillStyle = 'rgba(0, 255, 0, 0.3)';
      ctx.font = 'bold 20px Arial';
      ctx.fillText('PAUSED', canvas.width/2 - 50, canvas.height/2);
    }
  }
  
  draw();
  update();
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
