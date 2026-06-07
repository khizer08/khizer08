import requests

USERNAME = "khizer08"

# -----------------------------
# Fetch GitHub Data
# -----------------------------
user = requests.get(
    f"https://api.github.com/users/{USERNAME}"
).json()

repos = user.get("public_repos", 0)
followers = user.get("followers", 0)

# Total Stars
stars = 0

repos_data = requests.get(
    f"https://api.github.com/users/{USERNAME}/repos?per_page=100"
).json()

for repo in repos_data:
    stars += repo.get("stargazers_count", 0)

# Temporary values
streak = 108
contributions = 1027
active_days = 243

# -----------------------------
# SVG
# -----------------------------
svg = f"""
<svg width="1200" height="320" xmlns="http://www.w3.org/2000/svg">

<style>
.bg {{
    fill:#1a1b26;
}}

.outer {{
    fill:none;
    stroke:#bb9af7;
    stroke-width:2;
}}

.card {{
    fill:#24283b;
    stroke:#565f89;
    stroke-width:2;
}}

.title {{
    fill:#7aa2f7;
    font-size:36px;
    font-family:Arial;
    font-weight:bold;
}}

.value {{
    fill:#bb9af7;
    font-size:42px;
    font-family:Arial;
    font-weight:bold;
}}

.label {{
    fill:#73daca;
    font-size:18px;
    font-family:Arial;
}}

.icon {{
    font-size:42px;
}}
</style>

<!-- Background -->
<rect width="1200" height="320" class="bg"/>

<!-- Outer Border -->
<rect x="10" y="10"
      width="1180"
      height="300"
      rx="20"
      class="outer"/>

<!-- Title Lines -->
<line x1="170" y1="50"
      x2="350" y2="50"
      stroke="#bb9af7"
      stroke-width="2"/>

<line x1="850" y1="50"
      x2="1030" y2="50"
      stroke="#bb9af7"
      stroke-width="2"/>

<!-- Trophy -->
<text x="600"
      y="58"
      text-anchor="middle"
      class="title">
🏆 GitHub Trophies
</text>

<!-- Card 1 -->
<rect x="30" y="90" width="170" height="180" rx="15" class="card"/>
<text x="115" y="140" text-anchor="middle" class="icon">⭐</text>
<text x="115" y="200" text-anchor="middle" class="value">{stars}</text>
<text x="115" y="235" text-anchor="middle" class="label">Stars</text>

<!-- Card 2 -->
<rect x="220" y="90" width="170" height="180" rx="15" class="card"/>
<text x="305" y="140" text-anchor="middle" class="icon">🚀</text>
<text x="305" y="200" text-anchor="middle" class="value">{repos}</text>
<text x="305" y="235" text-anchor="middle" class="label">Repositories</text>

<!-- Card 3 -->
<rect x="410" y="90" width="170" height="180" rx="15" class="card"/>
<text x="495" y="140" text-anchor="middle" class="icon">👥</text>
<text x="495" y="200" text-anchor="middle" class="value">{followers}</text>
<text x="495" y="235" text-anchor="middle" class="label">Followers</text>

<!-- Card 4 -->
<rect x="600" y="90" width="170" height="180" rx="15" class="card"/>
<text x="685" y="140" text-anchor="middle" class="icon">🔥</text>
<text x="685" y="200" text-anchor="middle" class="value">{streak}</text>
<text x="685" y="235" text-anchor="middle" class="label">Streak</text>

<!-- Card 5 -->
<rect x="790" y="90" width="170" height="180" rx="15" class="card"/>
<text x="875" y="140" text-anchor="middle" class="icon">📈</text>
<text x="875" y="200" text-anchor="middle" class="value">{contributions}</text>
<text x="875" y="235" text-anchor="middle" class="label">Contributions</text>

<!-- Card 6 -->
<rect x="980" y="90" width="170" height="180" rx="15" class="card"/>
<text x="1065" y="140" text-anchor="middle" class="icon">📅</text>
<text x="1065" y="200" text-anchor="middle" class="value">{active_days}</text>
<text x="1065" y="235" text-anchor="middle" class="label">Active Days</text>

</svg>
"""

with open("trophy.svg", "w", encoding="utf-8") as f:
    f.write(svg)

print("trophy.svg generated successfully")