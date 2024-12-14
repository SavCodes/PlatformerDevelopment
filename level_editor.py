import pygame
import game_tile
import world_generator
import level_files
import copy
import button
from config import *
from main import load_sprite_sheets

def event_checker(level_editor):
    # =================== HOLDING KEY LOGIC ========================
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and level_editor.camera_x_position < SCREEN_WIDTH:
        level_editor.camera_x_position += 16
    elif keys[pygame.K_LEFT] and level_editor.camera_x_position > 0:
        level_editor.camera_x_position -= 16

    # =================== PRESSING KEY LOGIC =======================
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            return False
        # ============================= TOGGLE FOREGROUND ====================================
        if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
            level_editor.showing_foreground = not level_editor.showing_foreground
        # ============================= TOGGLE BACKGROUND ====================================
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_b:
            level_editor.showing_background = not level_editor.showing_background
        # ============================ TOGGLE TILE SETS ======================================
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_0:
            toggle_tilesets(level_editor, 0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_1:
            toggle_tilesets(level_editor, 1)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
            toggle_tilesets(level_editor, 2)
        # =========================== TOGGLE LEVELS ==========================================
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP and level_editor.current_level < len(level_files.player_one_level_set[0]) - 1:
            level_editor.current_level += 1
            level_editor.editing_array = [world_generator.WorldGenerator(level_files.player_one_level_set[0][level_editor.current_level]).world_tiles, "Level"]
            level_editor.editing_array[0] += level_editor.blank_array[(len(level_editor.editing_array[0]) - 1):]
            level_editor.foreground = world_generator.WorldGenerator(level_files.player_one_level_set[1][level_editor.current_level]).world_tiles
            level_editor.background = world_generator.WorldGenerator(level_files.player_one_level_set[2][level_editor.current_level]).world_tiles
            level_editor.level_title_button.set_text(f"Editing: Player {level_editor.selected_player} Level {level_editor.current_level} \n Layer: {level_editor.editing_array[1]}")
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN and level_editor.current_level > 0:
            level_editor.current_level -= 1
            level_editor.editing_array = [world_generator.WorldGenerator(level_files.player_one_level_set[0][level_editor.current_level]).world_tiles, "Level"]
            level_editor.editing_array[0] += level_editor.blank_array[(len(level_editor.editing_array[0]) - 1):]
            level_editor.foreground = world_generator.WorldGenerator(level_files.player_one_level_set[1][level_editor.current_level]).world_tiles
            level_editor.background = world_generator.WorldGenerator(level_files.player_one_level_set[2][level_editor.current_level]).world_tiles
            level_editor.level_title_button.set_text(f"Editing: Player {level_editor.selected_player} Level {level_editor.current_level} \n Layer: {level_editor.editing_array[1]}")
    return True

def create_button(x_scale, y_scale, text, screen, tile_set_image_width, width=100, height=40):
    x_position = tile_set_image_width * x_scale
    y_position = pygame.display.get_window_size()[1] * y_scale
    return button.Button(screen, x_position, y_position, width, height, text=text)

def toggle_tilesets(editor, tile_set_number):
    editor.current_tileset = tile_set_number
    editor.working_directory = editor.tile_set_directories[editor.current_tileset]
    editor.full_file_path =  editor.working_directory + editor.tile_set_name
    editor.tile_set_image = pygame.image.load(editor.full_file_path)
    if tile_set_number == 0:
        editor.starting_cols, editor.starting_rows = 12, 8
    elif tile_set_number == 1:
        editor.starting_cols, editor.starting_rows = 7, 7
    elif tile_set_number == 2:
        editor.starting_cols, editor.starting_rows = 4, 1
    editor.tile_set_image = pygame.transform.scale(editor.tile_set_image, (32 * editor.starting_cols, 32 * editor.starting_rows))
    editor.tile_set_image_width, editor.tile_set_image_height = editor.tile_set_image.get_width(), editor.tile_set_image.get_height()

class LevelEditor:
    def __init__(self):
        # ======================== needs to be sorted ============================
        pygame.init()
        pygame.display.set_caption('Level Editor')
        self.frame_rate = 300
        self.showing_foreground = False
        self.showing_background = False

        # ======================== CAMERA PANNING ATTRIBUTES ===================
        self.camera_y_position = 0
        self.camera_x_position = 0

        # ======================== FILE PATH ==================================
        self.current_tileset = 1
        self.starting_rows = 7
        self.starting_cols = 7
        self.tile_set_directories = [f"{DEFAULT_TILE_PATHS}tile_files/", f"{DEFAULT_TILE_PATHS}mossy_test/", f"{DEFAULT_TILE_PATHS}hazard_tiles/"]
        self.working_directory = self.tile_set_directories[self.current_tileset]              # CHANGE ME FOR DIFFERENT SETS
        self.tile_set_name = 'Tileset.png'                                                    # CHANGE ME FOR DIFFERENT SETS
        self.full_file_path = self.tile_set_directories[self.current_tileset] + self.tile_set_name
        self.tile_set_image = pygame.image.load(self.full_file_path)
        self.tile_set_image = pygame.transform.scale(self.tile_set_image,(32*self.starting_cols, 32*self.starting_rows))

        # ======================= SCREEN DATA =================================
        self.screen_width = PANNING_SCREEN_WIDTH
        self.screen_height = PANNING_SCREEN_HEIGHT
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        # ======================= TILE DATA ===================================
        self.tile_set_image_width = self.tile_set_image.get_width()
        self.tile_set_image_height = self.tile_set_image.get_height()
        self.selected_tile = None

        # ====================== LEVEL DATA ===================================
        self.grid_screen = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.level_x_length = (SCREEN_WIDTH - self.tile_set_image_width) // TILE_SIZE
        self.level_y_length = SCREEN_HEIGHT // TILE_SIZE

        # ==================== CREATE SETTING BUTTONS ===============================
        self.selected_player = "one"
        self.current_level = 1

        # Left sided buttons
        self.spawn_button = create_button(0.25, 0.50, "SET SPAWN", self.screen, self.tile_set_image_width)
        self.player_one_button = create_button(0.25, 0.60, "PLAYER ONE", self.screen, self.tile_set_image_width)
        self.save_button = create_button(0.25, 0.70, "SAVE LEVEL", self.screen, self.tile_set_image_width)
        self.background_button = create_button(0.25, 0.80, "BACKGROUND", self.screen, self.tile_set_image_width)

        # Right sided buttons
        self.objective_button = create_button(0.75, 0.50, "SET OBJECTIVE", self.screen, self.tile_set_image_width)
        self.player_two_button = create_button(0.75, 0.60, "PLAYER TWO", self.screen, self.tile_set_image_width)
        self.reset_button = create_button(0.75, 0.70, "RESET LEVEL", self.screen, self.tile_set_image_width)
        self.foreground_button = create_button(0.75, 0.80, "FOREGROUND", self.screen, self.tile_set_image_width)

        # Centered buttons
        self.level_title_button = create_button(0.45, 0.95, f"Editing: Player {self.selected_player} Level {self.current_level}", self.screen, self.tile_set_image_width)

        self.button_list = [
            self.spawn_button,
            self.player_one_button,
            self.player_two_button,
            self.save_button,
            self.background_button,
            self.objective_button,
            self.reset_button,
            self.foreground_button,
        ]

        # ==================== PLAYER SPAWN LOGIC ==================================
        self.player_spawn_set = False
        self.player_spawn_selected = False

        # ======================== CREATE BACKGROUND, FOREGROUND, AND PLAYER LEVEL =====================================
        self.background, self.player_tile, self.foreground = world_generator.generate_all_world_layers(level_files.player_one_level_set, scale=1, current_level=self.current_level)

        # ========================================= NEEDS SORTING =====================================================
        self.editing_array = [self.player_tile, "Player Level Tiles"]
        self.level_title_button.set_text(f"Editing: Player {self.selected_player} Level {self.current_level} \n Layer: {self.editing_array[1]}")

        self.level_blank = [[f"{self.working_directory}Tile_00.png" for i in range(self.level_x_length)] for j in range(self.level_y_length)]
        self.blank_array = world_generator.WorldGenerator(self.level_blank).world_tiles

        self.editing_array[0] += self.blank_array[(len(self.editing_array[0]) - 1):]
        self.original_level = copy.deepcopy(self.editing_array[0])
        self.tile_manager = self.load_and_scale_animated_tiles()

    # ========================== EDITING LOGIC METHODS ======================================
    def load_and_scale_animated_tiles(self):
        tile_manager = load_sprite_sheets()
        for tile in tile_manager.animated_background_tiles:
            tile["location"] = (tile["location"][0] / 2, tile["location"][1] / 2)
        for tile in tile_manager.animated_foreground_tiles:
            tile["location"] = (tile["location"][0] / 2, tile["location"][1] / 2)
        return tile_manager

    def select_tile(self):
        # Get mouse coordinates
        self.mouse_x , self.mouse_y = pygame.mouse.get_pos()

        # Check if mouse is in a location where a tile can be selected
        if self.mouse_x <= self.tile_set_image_width and self.mouse_y <= self.tile_set_image_height:
            x_tile_index = self.mouse_x // TILE_SIZE
            y_tile_index = self.mouse_y // TILE_SIZE

            # Select the hovered tile if left-mouse is clicked
            if pygame.mouse.get_just_pressed()[0]:
                self.selected_tile = x_tile_index + self.tile_set_image_width // TILE_SIZE * y_tile_index + 1
                self.selected_tile = f'0{self.selected_tile}' if len(str(self.selected_tile)) < 2 else self.selected_tile

    def add_to_level(self):
        # Leave if a tile is not selected, mouse is hovering the menu, or either mouse button was not pressed
        if not self.selected_tile or self.mouse_x <= self.tile_set_image_width or not pygame.mouse.get_pressed()[0] and not pygame.mouse.get_pressed()[2]:
            return
        
        # Format tile name to be saved into level data, select a blank tile is right mouse is clicked
        tile_file = f'{self.working_directory}Tile_{self.selected_tile}.png' if not pygame.mouse.get_pressed()[2] else self.working_directory + "Tile_00.png"

        # Add selected tile to the level data array
        level_x_index = (self.mouse_x + self.camera_x_position - self.tile_set_image_width) // TILE_SIZE
        level_y_index = self.mouse_y // TILE_SIZE
        self.editing_array[0][level_y_index][level_x_index] = game_tile.Platform(tile_file, level_x_index*TILE_SIZE, level_y_index*TILE_SIZE)

    def set_player_spawn(self):
        pygame.draw.circle(self.screen, "red", (self.mouse_x, self.mouse_y), 10)
        if pygame.mouse.get_pressed()[2]:
            self.player_spawn_selected = False

        if pygame.mouse.get_pressed()[0] and self.mouse_x > self.tile_set_image_width:
            level_x_index = (self.mouse_x + self.camera_x_position - self.tile_set_image_width) // TILE_SIZE
            level_y_index = self.mouse_y // TILE_SIZE
            print("x index: ", level_x_index)
            print("y index: ", level_y_index)
            self.player_spawn_selected = False

    def isolate_images(self, x_offset=0, y_offset=0, image_width=32, image_height=32):
        total_rows = self.tile_set_image_height // TILE_SIZE
        total_columns = self.tile_set_image_width // TILE_SIZE

        for j in range(total_rows):
            for i in range(total_columns):
                images = self.tile_set_image.subsurface(i*image_width+x_offset, min(j*image_height+y_offset, (total_rows-1)*image_height), image_width, image_height)
                tile_number = i + j * total_columns + 1
                if len(str(tile_number)) < 2:
                    tile_number = f'0{tile_number}'
                try:
                    pygame.image.save(images, f'Tile_{tile_number}.png')
                except Exception as e:
                    print(f"Error saving Tile_{tile_number}: {e}")
                print("File Saved: ", tile_number)

    # ============================= DISPLAY METHODS =========================================
    def display_gridlines(self):
        for j in range(self.level_y_length):
            for i in range(self.level_x_length):
                if (i + j) % 2 == 0:
                    color = (255,255,255)
                else:
                    color = (50,50,50)

                pygame.draw.rect(self.grid_screen, color,
                                 (i * TILE_SIZE, j * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    def display_tile(self, array_to_display):
        start_index = self.camera_x_position // TILE_SIZE
        end_index = (self.screen_width - self.tile_set_image_width) // TILE_SIZE + start_index
        for layer in array_to_display:
            for tile in layer[start_index:end_index]:
                tile.draw_platform(self.grid_screen)

    def display_buttons(self):
        for menu_button in self.button_list:
            menu_button.display_button()

    # ============================ BUTTON METHODS ===========================================
    def check_spawn_button(self):
        self.spawn_button.check_pressed(self.mouse_x, self.mouse_y)
        if self.spawn_button.is_pressed:
            self.player_spawn_selected = True

    def check_player_buttons(self):
        # Player one click detection
        self.player_one_button.check_pressed(self.mouse_x, self.mouse_y)
        if self.player_one_button.is_pressed:
            self.selected_player = "one"
            self.level_title_button.display_button()
            self.editing_array =  [self.player_tile, "Player Level Tiles"]

            self.level_title_button.set_text(f"Editing: Player {self.selected_player} Level {self.current_level} \n Layer: {self.editing_array[1]}")

        # Player two click detection
        self.player_two_button.check_pressed(self.mouse_x, self.mouse_y)
        if self.player_two_button.is_pressed:
            self.selected_player = "two"
            self.editing_array =  [self.player_tile, "Player Level Tiles"]
            self.level_title_button.set_text(f"Editing: Player {self.selected_player} Level {self.current_level} \n Layer: {self.editing_array[1]}")

    def check_save_button(self):
        # Check if mouse is hovering button
        self.save_button.check_pressed(self.mouse_x, self.mouse_y)
        if self.save_button.is_pressed:
            with open("new_levels.md", "a") as file:
                file.write("###")
                file.write(f"player_{self.selected_player}_{self.editing_array[1].split()[0]}_{self.current_level} = [ \n")
                for row in self.editing_array[0]:
                    file.write(f'{row},')
                file.write("] \n")
            self.save_button.is_pressed = False

    def check_reset_button(self):
        self.reset_button.check_pressed(self.mouse_x, self.mouse_y)
        if self.reset_button.is_pressed:
            self.editing_array[0] = copy.deepcopy(self.original_level)

    def check_foreground_button(self):
        self.foreground_button.check_pressed(self.mouse_x, self.mouse_y)
        if self.foreground_button.is_pressed:
            self.editing_array = [self.foreground, "Foreground Layer"]
            self.level_title_button.set_text(f"Editing: Player {self.selected_player} Level {self.current_level} \n Layer: {self.editing_array[1]}")

    def check_background_button(self):
        self.background_button.check_pressed(self.mouse_x, self.mouse_y)
        if self.background_button.is_pressed:
            self.editing_array = [self.background, "Background Layer"]
            self.level_title_button.set_text(f"Editing: Player {self.selected_player} Level {self.current_level} \n Layer: {self.editing_array[1]}")

    def pan_camera(self):
        panning_display_rect = pygame.Rect(self.camera_x_position,0, PANNING_SCREEN_WIDTH,PANNING_SCREEN_HEIGHT)
        self.screen.blit(self.grid_screen, (self.tile_set_image_width,0), area=panning_display_rect)

def main():
    level_editor = LevelEditor()
    #level_editor.isolate_images(0, 0)
    clock = pygame.Clock()
    frame_rate = 300
    running = True

    while running:
        # ================================== LOGIC RELATED CODE ====================================
        running = event_checker(level_editor)
        level_editor.add_to_level()
        level_editor.select_tile()

        # ================================== DISPLAY RELATED CODE ==================================
        level_editor.grid_screen.fill((0,0,0))
        level_editor.screen.fill((0, 0, 0))
        level_editor.display_gridlines()
        level_editor.screen.blit(level_editor.grid_screen, (level_editor.tile_set_image_width, 0))
        level_editor.tile_manager.draw_tiles(level_editor.grid_screen, level_editor.tile_manager.animated_background_tiles)

        # BACKGROUND DISPLAY TOGGLE
        if level_editor.showing_background:
            level_editor.display_tile(level_editor.background)
            level_editor.tile_manager.draw_tiles(level_editor.grid_screen, level_editor.tile_manager.animated_background_tiles)

        # PLAYER LEVEL DISPLAY
        level_editor.display_tile(level_editor.player_tile)

        # FOREGROUND DISPLAY TOGGLE
        if level_editor.showing_foreground:
            level_editor.display_tile(level_editor.foreground)
            level_editor.tile_manager.draw_tiles(level_editor.grid_screen, level_editor.tile_manager.animated_foreground_tiles)

        level_editor.pan_camera()
        level_editor.screen.blit(level_editor.tile_set_image)

        # ================================= BUTTON DISPLAY CODE ===================================
        level_editor.display_buttons()

        # ================================ BUTTON LOGIC CODE =====================================
        level_editor.check_save_button()
        level_editor.check_player_buttons()
        level_editor.check_reset_button()
        level_editor.check_spawn_button()
        level_editor.check_foreground_button()
        level_editor.check_background_button()

        if level_editor.player_spawn_selected:
            level_editor.set_player_spawn()

        clock.tick(frame_rate)
        pygame.display.update()

if __name__ == '__main__':
    main()
    pygame.quit()
