# npc.py
import random

class NPC:
    def __init__(self, name, personality):
        self.name = name
        self.personality = personality
        self.hunger = 100
        self.thirst = 100
        self.social_needs = 100
        self.relationships = {}
        self.is_alive = True
        self.position = (random.randint(0, 800), random.randint(0, 600))
        self.job = None
        self.family = []
        self.desires = []

    def update_needs(self):
        """Update NPC needs each game cycle."""
        self.hunger -= random.randint(1, 5)
        self.thirst -= random.randint(1, 5)
        self.social_needs -= random.randint(1, 3)
        
        if self.hunger <= 0 or self.thirst <= 0:
            self.is_alive = False
        
        if self.hunger < 50:
            self.desires.append("Find Food")
        if self.thirst < 50:
            self.desires.append("Find Water")

    def interact(self, other_npc):
        """Define how NPC interacts with another NPC based on personality."""
        interaction_outcome = random.choice(["friendship", "rivalry", "neutral"])
        if interaction_outcome == "friendship":
            self.relationships[other_npc.name] = "friend"
        elif interaction_outcome == "rivalry":
            self.relationships[other_npc.name] = "rival"
        else:
            self.relationships[other_npc.name] = "neutral"

    def move(self):
        """NPC moves randomly in the world."""
        x, y = self.position
        self.position = (x + random.randint(-5, 5), y + random.randint(-5, 5))

    def take_job(self, job):
        """Assign job to NPC."""
        self.job = job

    def work(self):
        """Perform job actions."""
        if self.job:
            print(f"{self.name} is working as a {self.job}.")

    def form_family(self, partner):
        """Form a family with another NPC."""
        if "friend" in self.relationships.get(partner.name, ""):
            self.family.append(partner)
            partner.family.append(self)

    def __str__(self):
        return f"NPC: {self.name}, Hunger: {self.hunger}, Thirst: {self.thirst}, Social: {self.social_needs}"
# world.py
import random
import pygame

class World:
    def __init__(self, screen):
        self.screen = screen
        self.npcs = []
        self.buildings = []
        self.generate_town()

    def generate_town(self):
        """Randomly generate the town with buildings and NPCs."""
        for _ in range(10):  # Create 10 buildings
            x, y = random.randint(0, 800), random.randint(0, 600)
            building = pygame.Rect(x, y, 50, 50)
            self.buildings.append(building)

        for _ in range(20):  # Create 20 NPCs
            name = f"NPC_{random.randint(1, 1000)}"
            personality = {
                "openness": random.randint(1, 100),
                "conscientiousness": random.randint(1, 100),
                "extraversion": random.randint(1, 100),
                "agreeableness": random.randint(1, 100),
                "neuroticism": random.randint(1, 100),
            }
            npc = NPC(name, personality)
            self.npcs.append(npc)

    def update(self):
        """Update the world state."""
        for npc in self.npcs:
            if npc.is_alive:
                npc.update_needs()
                npc.move()
                # Handle NPC jobs and interactions
                npc.work()

    def draw(self):
        """Draw the world elements."""
        for building in self.buildings:
            pygame.draw.rect(self.screen, (100, 100, 100), building)

        for npc in self.npcs:
            if npc.is_alive:
                pygame.draw.circle(self.screen, (0, 255, 0), npc.position, 5)
            else:
                pygame.draw.circle(self.screen, (255, 0, 0), npc.position, 5)
# economy.py
class Job:
    def __init__(self, name, wage):
        self.name = name
        self.wage = wage

class Economy:
    def __init__(self):
        self.available_jobs = []

    def create_jobs(self):
        """Generate jobs like farmer, trader, builder."""
        self.available_jobs = [
            Job("Farmer", 10),
            Job("Trader", 15),
            Job("Builder", 12),
            Job("Leader", 20)
        ]

    def assign_job(self, npc):
        """Assign an available job to an NPC."""
        job = random.choice(self.available_jobs)
        npc.take_job(job.name)
# main.py
import pygame
from world import World
from economy import Economy

pygame.init()

# Game setup
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Dynamic Towns")
clock = pygame.time.Clock()

# World and economy initialization
world = World(screen)
economy = Economy()
economy.create_jobs()

# Main game loop
running = True
while running:
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    world.update()
    world.draw()
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
# npc.py
from typing import Dict, List, Tuple
import random

class NPC:
    def __init__(self, name: str, personality: Dict[str, int]):
        self.name: str = name
        self.personality: Dict[str, int] = personality
        self.hunger: int = 100
        self.thirst: int = 100
        self.social_needs: int = 100
        self.relationships: Dict[str, str] = {}
        self.is_alive: bool = True
        self.position: Tuple[int, int] = (random.randint(0, 800), random.randint(0, 600))
        self.job: str = None
        self.family: List[NPC] = []
        self.desires: List[str] = []

    def update_needs(self) -> None:
        """Update NPC needs each game cycle."""
        self.hunger -= random.randint(1, 5)
        self.thirst -= random.randint(1, 5)
        self.social_needs -= random.randint(1, 3)

        if self.hunger <= 0 or self.thirst <= 0:
            self.is_alive = False

        if self.hunger < 50:
            self.desires.append("Find Food")
        if self.thirst < 50:
            self.desires.append("Find Water")

    def interact(self, other_npc: 'NPC') -> None:
        """Define how NPC interacts with another NPC based on personality."""
        interaction_outcome: str = random.choice(["friendship", "rivalry", "neutral"])
        if interaction_outcome == "friendship":
            self.relationships[other_npc.name] = "friend"
        elif interaction_outcome == "rivalry":
            self.relationships[other_npc.name] = "rival"
        else:
            self.relationships[other_npc.name] = "neutral"

    def move(self) -> None:
        """NPC moves randomly in the world."""
        x, y = self.position
        self.position = (x + random.randint(-5, 5), y + random.randint(-5, 5))

    def take_job(self, job: str) -> None:
        """Assign job to NPC."""
        self.job = job

    def work(self) -> None:
        """Perform job actions."""
        if self.job:
            print(f"{self.name} is working as a {self.job}.")

    def form_family(self, partner: 'NPC') -> None:
        """Form a family with another NPC."""
        if "friend" in self.relationships.get(partner.name, ""):
            self.family.append(partner)
            partner.family.append(self)

    def __str__(self) -> str:
        return f"NPC: {self.name}, Hunger: {self.hunger}, Thirst: {self.thirst}, Social: {self.social_needs}"
# world.py
from typing import List
import pygame
import random
from npc import NPC

class World:
    def __init__(self, screen: pygame.Surface):
        self.screen: pygame.Surface = screen
        self.npcs: List[NPC] = []
        self.buildings: List[pygame.Rect] = []
        self.generate_town()

    def generate_town(self) -> None:
        """Randomly generate the town with buildings and NPCs."""
        for _ in range(10):  # Create 10 buildings
            x, y = random.randint(0, 800), random.randint(0, 600)
            building = pygame.Rect(x, y, 50, 50)
            self.buildings.append(building)

        for _ in range(20):  # Create 20 NPCs
            name = f"NPC_{random.randint(1, 1000)}"
            personality = {
                "openness": random.randint(1, 100),
                "conscientiousness": random.randint(1, 100),
                "extraversion": random.randint(1, 100),
                "agreeableness": random.randint(1, 100),
                "neuroticism": random.randint(1, 100),
            }
            npc = NPC(name, personality)
            self.npcs.append(npc)

    def update(self) -> None:
        """Update the world state."""
        for npc in self.npcs:
            if npc.is_alive:
                npc.update_needs()
                npc.move()
                npc.work()

    def draw(self) -> None:
        """Draw the world elements."""
        for building in self.buildings:
            pygame.draw.rect(self.screen, (100, 100, 100), building)

        for npc in self.npcs:
            if npc.is_alive:
                pygame.draw.circle(self.screen, (0, 255, 0), npc.position, 5)
            else:
                pygame.draw.circle(self.screen, (255, 0, 0), npc.position, 5)
# test_npc.py
import unittest
from npc import NPC

class TestNPC(unittest.TestCase):

    def setUp(self):
        """Set up test environment."""
        personality = {
            "openness": 70,
            "conscientiousness": 60,
            "extraversion": 50,
            "agreeableness": 80,
            "neuroticism": 40,
        }
        self.npc = NPC(name="TestNPC", personality=personality)

    def test_update_needs(self):
        """Test if NPC needs are updated."""
        initial_hunger = self.npc.hunger
        self.npc.update_needs()
        self.assertLess(self.npc.hunger, initial_hunger, "Hunger should decrease over time.")

    def test_interact(self):
        """Test if NPC can interact and form relationships."""
        other_npc = NPC(name="OtherNPC", personality=self.npc.personality)
        self.npc.interact(other_npc)
        self.assertIn(other_npc.name, self.npc.relationships, "NPC should have formed a relationship.")

    def test_move(self):
        """Test NPC movement."""
        initial_position = self.npc.position
        self.npc.move()
        self.assertNotEqual(self.npc.position, initial_position, "NPC should move.")

if __name__ == "__main__":
    unittest.main()
# test_world.py
import unittest
import pygame
from world import World

class TestWorld(unittest.TestCase):

    def setUp(self):
        """Set up test environment with a mock screen."""
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.world = World(self.screen)

    def test_generate_town(self):
        """Test if town and NPCs are generated."""
        self.assertGreater(len(self.world.npcs), 0, "There should be NPCs in the town.")
        self.assertGreater(len(self.world.buildings), 0, "There should be buildings in the town.")

    def test_world_update(self):
        """Test world update mechanics."""
        initial_positions = [npc.position for npc in self.world.npcs]
        self.world.update()
        for i, npc in enumerate(self.world.npcs):
            self.assertNotEqual(npc.position, initial_positions[i], "NPCs should move in the world.")

if __name__ == "__main__":
    unittest.main()
# npc.py
class NPC:
    def __init__(self, name: str, personality: Dict[str, int]):
        self.name: str = name
        self.personality: Dict[str, int] = personality
        self.hunger: int = 100
        self.thirst: int = 100
        self.social_needs: int = 100
        self.relationships: Dict[str, str] = {}
        self.is_alive: bool = True
        self.position: Tuple[int, int] = (random.randint(0, 800), random.randint(0, 600))
        self.job: str = None
        self.family: List[NPC] = []
        self.desires: List[str] = []
        self.faction: str = None  # NPC can belong to a faction

    def join_faction(self, faction: str) -> None:
        """NPC joins a faction."""
        self.faction = faction

    def interact(self, other_npc: 'NPC') -> None:
        """Define how NPC interacts with another NPC based on personality and faction."""
        interaction_outcome = random.choice(["friendship", "rivalry", "neutral"])
        if interaction_outcome == "friendship":
            self.relationships[other_npc.name] = "friend"
        elif interaction_outcome == "rivalry":
            if self.faction and other_npc.faction and self.faction != other_npc.faction:
                self.relationships[other_npc.name] = "rival (factional)"
            else:
                self.relationships[other_npc.name] = "rival"
        else:
            self.relationships[other_npc.name] = "neutral"
