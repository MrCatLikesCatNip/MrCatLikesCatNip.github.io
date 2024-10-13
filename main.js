// Constants for game
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');
const TILE_SIZE = 40; // Each grid square is 40x40 pixels
const GRID_SIZE = 20; // 20x20 grid
const NPC_COUNT = 10; // Initial number of NPCs

// World setup (2D grid)
let world = [];
for (let i = 0; i < GRID_SIZE; i++) {
    world[i] = [];
    for (let j = 0; j < GRID_SIZE; j++) {
        world[i][j] = { type: 'empty', occupants: [] }; // Each cell in the world can hold NPCs or buildings
    }
}

// Define NPC personalities
const PERSONALITIES = ['friendly', 'aggressive', 'ambitious', 'lazy', 'curious'];
const JOBS = ['farmer', 'trader', 'builder', 'leader', 'none'];

// NPC class
class NPC {
    constructor(name, x, y) {
        this.name = name;
        this.x = x;
        this.y = y;
        this.hunger = 100;
        this.thirst = 100;
        this.personality = PERSONALITIES[Math.floor(Math.random() * PERSONALITIES.length)];
        this.job = JOBS[Math.floor(Math.random() * JOBS.length)];
        this.relationships = [];
    }

    // NPC Movement
    move() {
        const dx = Math.floor(Math.random() * 3) - 1; // Random move: -1, 0, or 1
        const dy = Math.floor(Math.random() * 3) - 1;
        this.x = Math.max(0, Math.min(GRID_SIZE - 1, this.x + dx));
        this.y = Math.max(0, Math.min(GRID_SIZE - 1, this.y + dy));
    }

    // Social Interactions
    interact(npc) {
        if (this.personality === 'friendly') {
            this.relationships.push({ npc: npc.name, status: 'friend' });
        } else if (this.personality === 'aggressive') {
            this.relationships.push({ npc: npc.name, status: 'rival' });
        }
    }

    // NPC Needs: Hunger and Thirst
    updateNeeds() {
        this.hunger -= 1;
        this.thirst -= 1;

        if (this.hunger <= 0 || this.thirst <= 0) {
            console.log(`${this.name} has died from hunger or thirst!`);
        }
    }

    // Render NPC on the canvas
    render() {
        ctx.fillStyle = 'blue';
        ctx.fillRect(this.x * TILE_SIZE, this.y * TILE_SIZE, TILE_SIZE, TILE_SIZE);
    }
}

// Initialize NPCs
let npcs = [];
for (let i = 0; i < NPC_COUNT; i++) {
    const name = `NPC${i + 1}`;
    const x = Math.floor(Math.random() * GRID_SIZE);
    const y = Math.floor(Math.random() * GRID_SIZE);
    const npc = new NPC(name, x, y);
    npcs.push(npc);
    world[x][y].occupants.push(npc);
}

// Update game state
function updateGameState() {
    npcs.forEach(npc => {
        npc.move();
        npc.updateNeeds();

        // Check for interactions with other NPCs
        npcs.forEach(other => {
            if (npc !== other && npc.x === other.x && npc.y === other.y) {
                npc.interact(other);
            }
        });
    });
}

// Render world and NPCs
function renderWorld() {
    // Clear canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Render grid
    for (let i = 0; i < GRID_SIZE; i++) {
        for (let j = 0; j < GRID_SIZE; j++) {
            ctx.strokeStyle = 'gray';
            ctx.strokeRect(i * TILE_SIZE, j * TILE_SIZE, TILE_SIZE, TILE_SIZE);
        }
    }

    // Render NPCs
    npcs.forEach(npc => npc.render());
}

// Main game loop
function gameLoop() {
    updateGameState();
    renderWorld();
    requestAnimationFrame(gameLoop);
}

// Start the game loop
gameLoop();
