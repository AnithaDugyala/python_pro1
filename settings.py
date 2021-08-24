class Settings:
	def __init__(self):
		self.screen_width=1200
		self.screen_height=800
		self.bg_color=(230,230,230)

		self.ship_limit=3

		self.bullet_width=100
		self.bullet_height=15
		self.bullet_color=(60,60,60)
		self.bullets_allowed=4

		self.fleet_drop_speed=3
	 
		self.speedup_scale=1.1  ##2 indicates doubles the speed, 1 indicates constant speed and 1.1 is between 2 and 1
		self.scoreup_scale=1.5
		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		self.ship_speed=1.5
		self.bullet_speed=3.0
		self.alien_speed=2.0
		self.fleet_direction=1   ##1 indicates right direction
		self.alien_points=50

	def increase_speed(self):  ##to increase speed after a level reaches
		self.ship_speed*=self.speedup_scale
		self.bullet_speed*=self.speedup_scale
		self.alien_speed*=self.speedup_scale
		self.alien_points=int(self.alien_points*self.scoreup_scale) ##integer value
		print(self.alien_points)
