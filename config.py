# =========================== DECLARATION OF GAME CONSTANTS ===============================
GAME_SCALE = 2
TILE_SIZE = 32
PANNING_SCREEN_WIDTH = 960
PANNING_SCREEN_HEIGHT = 640
X_WINDOW_PANNING_INDEX = PANNING_SCREEN_WIDTH // (TILE_SIZE * 2 * GAME_SCALE) + 1
Y_WINDOW_PANNING_INDEX = PANNING_SCREEN_HEIGHT // (TILE_SIZE * 4 * GAME_SCALE) + 1
SCREEN_WIDTH = PANNING_SCREEN_WIDTH * 5
SCREEN_HEIGHT = PANNING_SCREEN_HEIGHT * 3
PLAYER_OFFSET_Y = 400
BACKGROUND_SCROLL_FACTOR = 0.1

DEFAULT_FONT = "C:/Users/Josep/PycharmProjects/PlatformerTrialRun/game_assets/fonts/ByteBounce.ttf"
DEFAULT_TEXT_COLOR = (30, 30, 30)  # Black


# ========================= GAME ASSET LOCATIONS ============================================
DEFAULT_TILE_PATHS = "C:/Users/Josep/PycharmProjects/PlatformerTrialRun/game_assets/tile_sets"
DEFAULT_BACKGROUND_IMAGE_PATH = "C:/Users/Josep/PycharmProjects/PlatformerTrialRun/game_assets/background_images"
DEFAULT_NPC_SPRITESHEET_PATH = "C:/Users/Josep/PycharmProjects/PlatformerTrialRun/game_assets/spritesheets/npc_spritesheets/"
DEFAULT_PLAYER_SPRITESHEET_PATH = "C:/Users/Josep/PycharmProjects/PlatformerTrialRun/game_assets/spritesheets/player_spritesheets/"
