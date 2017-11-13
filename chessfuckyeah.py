import os
game = True
board = [' _ '] * 64
white_pieces = ['wR1', 'wK1', 'wB1', 'wQ', 'wKI', 'wB2', 'wK2', 'wR2','wP1', 'wP2', 'wP3', 'wP4', 'wP5', 'wP6', 'wP7', 'wP8']
black_pieces = ['bP1', 'bP2', 'bP3', 'bP4', 'bP5', 'bP6', 'bP7', 'bP8', 'bR1', 'bK1', 'bB1', 'bQ', 'bKI', 'bB2', 'bK2', 'bR2']
white_captured = []
black_captured = []
knight_moves = [-15, -17, -10, 6, 15, 17, 10, -6]
bishop_moves = [7, 9, -7, -9]
rook_moves = [8, -8, 1, -1]
king_moves = [8, -8, 1, -1, 7, 9, -7, -9]
move = 0
pick = 0
pickt = "Choose position to move piece: "


for i in range(16):
	board[i] = white_pieces[i]

for i in range(48,64):
	board[i] = black_pieces[i-48]

def revive(self,pos,name):
	if self == "black":
		revive = raw_input("please choose the piece you want to revive: ")
		for i in black_captured:
			if revive == i:
				black_captured.append(board[pos])
				board[pos] = i
				black_captured.remove(board[pos])
	if self == "white":
		revive = raw_input("please choose the piece you want to revive: ")
		for i in white_captured:
			if revive == i:
				white_captured.append(board[pos])
				board[pos] = i
				white_captured.remove(board[pos])
				
				
				

def show():
	printx = 0
	printy = 8
	printl = 0
	print("     1      2      3      4      5      6      7      8")
	for i in range(8):
		if printl == 0:
			print(" A " + str(board[printx:printy]))
			print ("")
			print ("")
		if printl == 1:
			print(" B " + str(board[printx:printy]))
			print ("")
			print ("")
		if printl == 2:
			print(" C " + str(board[printx:printy]))
			print ("")
			print ("")
		if printl == 3:
			print(" D " + str(board[printx:printy]))
			print ("")
			print ("")
		if printl == 4:
			print(" E " + str(board[printx:printy]))
			print ("")
			print ("")
		if printl == 5:
			print(" F " + str(board[printx:printy]))
			print ("")
			print ("")
		if printl == 6:
			print(" G " + str(board[printx:printy]))
			print ("")
			print ("")
		if printl == 7:
			print(" H " + str(board[printx:printy]))
			print ("")
			print ("")
		printx += 8
		printy += 8
		printl += 1
	print("White pieces captured" + str(white_captured))
	print("Black pieces captured" + str(black_captured))
		
def translate(self):
	if self == 'a1':
		return 0
	elif self == 'a2':
		return 1
	elif self == 'a3':
		return 2
	elif self == 'a4':
		return 3
	elif self == 'a5':
		return 4
	elif self == 'a6':
		return 5
	elif self == 'a7':
		return 6
	elif self == 'a8':
		return 7
	elif self == 'b1':
		return 8
	elif self == 'b2':
		return 9
	elif self == 'b3':
		return 10
	elif self == 'b4':
		return 11
	elif self == 'b5':
		return 12
	elif self == 'b6':
		return 13
	elif self == 'b7':
		return 14
	elif self == 'b8':
		return 15
	elif self == 'c1':
		return 16
	elif self == 'c2':
		return 17
	elif self == 'c3':
		return 18
	elif self == 'c4':
		return 19
	elif self == 'c5':
		return 20
	elif self == 'c6':
		return 21
	elif self == 'c7':
		return 22
	elif self == 'c8':
		return 23
	elif self == 'd1':
		return 24
	elif self == 'd2':
		return 25
	elif self == 'd3':
		return 26
	elif self == 'd4':
		return 27
	elif self == 'd5':
		return 28
	elif self == 'd6':
		return 29
	elif self == 'd7':
		return 30
	elif self == 'd8':
		return 31
	elif self == 'e1':
		return 32
	elif self == 'e2':
		return 33
	elif self == 'e3':
		return 34
	elif self == 'e4':
		return 35
	elif self == 'e5':
		return 36
	elif self == 'e6':
		return 37
	elif self == 'e7':
		return 38
	elif self == 'e8':
		return 39
	elif self == 'f1':
		return 40
	elif self == 'f2':
		return 41
	elif self == 'f3':
		return 42
	elif self == 'f4':
		return 43
	elif self == 'f5':
		return 44
	elif self == 'f6':
		return 45
	elif self == 'f7':
		return 46
	elif self == 'f8':
		return 47
	elif self == 'g1':
		return 48
	elif self == 'g2':
		return 49
	elif self == 'g3':
		return 50
	elif self == 'g4':
		return 51
	elif self == 'g5':
		return 52
	elif self == 'g6':
		return 53
	elif self == 'g7':
		return 54
	elif self == 'g8':
		return 55
	elif self == 'h1':
		return 56
	elif self == 'h2':
		return 57
	elif self == 'h3':
		return 58
	elif self == 'h4':
		return 59
	elif self == 'h5':
		return 60
	elif self == 'h6':
		return 61
	elif self == 'h7':
		return 62
	elif self == 'h8':
		return 63
	else:
		for i in range(64):
			if board[i] == " _ ":
				return i

class captured(object):
	global white_captured
	global black_captured
	
	def __init__(self, name):
		self.name = name
		
	def capture(self):
		if 'w' in self.name:
			white_captured.append(self.name)
		elif 'b' in self.name:
			black_captured.append(self.name)
			
class pking(object):
	global board
	global king_moves
	
	def __init__(self,posold,posnew,name):
		self.posold = posold
		self.posnew = posnew
		self.name = name
		
	def move(self):
		for i in king_moves:
			if self.posnew - self.posold == i:
				if 'w' not in self.name and 'w' in board[self.posnew]:
					cap = captured(board[self.posnew])
					cap.capture()
					board[self.posnew] = self.name
					board[self.posold] = " _ "
				elif 'b' not in self.name and 'b' in board[self.posnew]:
					cap = captured(board[self.posnew])
					cap.capture()
					board[self.posnew] = self.name
					board[self.posold] = " _ "
				elif board[self.posnew] == " _ ":
					board[self.posnew] = self.name
					board[self.posold] = " _ "
			
			
			
class pqueen(object):
	global board
	global king_moves
	
	def __init__(self,posold,posnew,name):
		self.posold = posold
		self.posnew = posnew
		self.name = name
		
	def move(self):
		for i in king_moves:
			picked_move = i
			x = self.posold + picked_move
			y = self.posnew
			f = True
			if x > y:
				temp = x
				x = y
				y = temp
			if picked_move > 0:
				if (x - y) % picked_move == 0:
					while x != y:
						if board[x] != " _ ":
							f = False
						x += picked_move
						
					if f == True and 'w' not in self.name and 'w' in board[self.posnew]:
						cap = captured(board[self.posnew])
						cap.capture()
						board[self.posnew] = self.name
						board[self.posold] = " _ "
					elif f == True and 'b' not in self.name and 'b' in board[self.posnew]:
						cap = captured(board[self.posnew])
						cap.capture()
						board[self.posnew] = self.name
						board[self.posold] = " _ "
					elif f == True and board[self.posnew] == " _ ":
						board[self.posnew] = self.name
						board[self.posold] = " _ "
			
			elif picked_move < 0:
				picked_move = -picked_move
				if (x - y) % picked_move == 0:
					while x != y:
						if board[x + picked_move] != " _ ":
							f = False
						x += picked_move
						
					if f == True and 'w' not in self.name and 'w' in board[self.posnew]:
						cap = captured(board[self.posnew])
						cap.capture()
						board[self.posnew] = self.name
						board[self.posold] = " _ "
					elif f == True and 'b' not in self.name and 'b' in board[self.posnew]:
						cap = captured(board[self.posnew])
						cap.capture()
						board[self.posnew] = self.name
						board[self.posold] = " _ "
					elif f == True and board[self.posnew] == " _ ":
						board[self.posnew] = self.name
						board[self.posold] = " _ "
	
			
class prook(object):
	global board
	global rook_moves
	
	def __init__(self,posold,posnew,name):
		self.posold = posold
		self.posnew = posnew
		self.name = name
		
	def move(self):
		
		for i in rook_moves:
			picked_move = i
			x = self.posold + picked_move
			y = self.posnew
			f = True
			
			if x > y:
				temp = x
				x = y
				y = temp
			if picked_move > 0:
				if (x - y) % picked_move == 0:
					while x != y:
						if board[x] != " _ ":
							f = False
						x += picked_move
						
					if f == True and 'w' not in self.name and 'w' in board[self.posnew]:
						cap = captured(board[self.posnew])
						cap.capture()
						board[self.posnew] = self.name
						board[self.posold] = " _ "
					elif f == True and 'b' not in self.name and 'b' in board[self.posnew]:
						cap = captured(board[self.posnew])
						cap.capture()
						board[self.posnew] = self.name
						board[self.posold] = " _ "
					elif f == True and board[self.posnew] == " _ ":
						board[self.posnew] = self.name
						board[self.posold] = " _ "
			
			elif picked_move < 0:
				picked_move = -picked_move
				if (x - y) % picked_move == 0:
					while x != y:
						if board[x + picked_move] != " _ ":
							f = False
						x += picked_move
						
					if f == True and 'w' not in self.name and 'w' in board[self.posnew]:
						cap = captured(board[self.posnew])
						cap.capture()
						board[self.posnew] = self.name
						board[self.posold] = " _ "
					elif f == True and 'b' not in self.name and 'b' in board[self.posnew]:
						cap = captured(board[self.posnew])
						cap.capture()
						board[self.posnew] = self.name
						board[self.posold] = " _ "
					elif f == True and board[self.posnew] == " _ ":
						board[self.posnew] = self.name
						board[self.posold] = " _ "
							
			
			
						

class pbishop(object):
	global board
	global bishop_moves
	
	def __init__(self,posold,posnew,name):
		self.posold = posold
		self.posnew = posnew
		self.name = name
	
	def move(self):
		for i in bishop_moves:
			picked_move = i
			x = self.posold + picked_move
			y = self.posnew
			f = True
			
			if x > y:
				temp = x
				x = y
				y = temp
				
			if picked_move > 0:
				if (x - y) % picked_move == 0:
					while x != y:
						if board[x] != " _ ":
							f = False
						print x
						print y
						print picked_move
						x += picked_move

					if f == True and board[self.posnew] == " _ ":
						board[self.posnew] = self.name
						board[self.posold] = " _ "
					elif 'w' in self.name and 'b' in board[self.posnew] and f == True:
						cap = captured(board[self.posnew])
						cap.capture()
						board[self.posnew] = self.name
						board[self.posold] = " _ "
					elif 'b' in self.name and 'w' in board[self.posnew] and f == True:
						cap = captured(board[self.posnew])
						cap.capture()
						board[self.posnew] = self.name
						board[self.posold] = " _ " 
			elif picked_move < 0:
				picked_move = -picked_move
				if (x - y) % picked_move == 0:
					while x != y:
						if board[x + picked_move] != " _ ":
							f = False
						print x
						print y
						print picked_move
						x += picked_move

					if f == True and board[self.posnew] == " _ ":
						board[self.posnew] = self.name
						board[self.posold] = " _ "
					elif 'w' in self.name and 'b' in board[self.posnew] and f == True:
						cap = captured(board[self.posnew])
						cap.capture()
						board[self.posnew] = self.name
						board[self.posold] = " _ "
					elif 'b' in self.name and 'w' in board[self.posnew] and f == True:
						cap = captured(board[self.posnew])
						cap.capture()
						board[self.posnew] = self.name
						board[self.posold] = " _ " 
		

class pknight(object):
	global board
	global knight_moves
	
	def __init__(self,posold,posnew,name):
		self.posold = posold
		self.posnew = posnew
		self.name = name

	def move(self):
		for i in knight_moves:
			if self.posold == self.posnew + i and self.posnew > 0 and self.posnew < 65:
				if 'w' in self.name:
					if 'b' in board[self.posnew]:
						cap = captured(board[self.posnew])
						cap.capture()
						board[self.posnew] = self.name
						board[self.posold] = " _ "
					else:
						board[self.posnew] = self.name
						board[self.posold] = " _ "
				elif 'b' in self.name:
					if 'w' in board[self.posnew]:
						cap = captured(board[self.posnew])
						cap.capture()
						board[self.posnew] = self.name
						board[self.posold] = " _ "
					else:
						board[self.posnew] = self.name
						board[self.posold] = " _ "
		
class white_pawn(object):
	global board
	
	
	def __init__(self,posold,posnew,name):
		self.posold = posold
		self.posnew = posnew
		self.name = name
		
	def move(self):
		if self.posold == self.posnew -8 and board[self.posnew] == " _ ":
				board[self.posold] = " _ "
				board[self.posnew] = self.name
		elif self.posold == self.posnew -16 and board[self.posnew] == " _ ":
			for i in range(8,16):
				if self.posold == i:
					board[self.posold] = " _ "
					board[self.posnew] = self.name
		elif (self.posold == self.posnew - 7 and board[self.posnew] != " _ ") or (self.posold == self.posnew -9 and board[self.posnew] != " _ " and 'w' not in board[self.posnew]):
			cap = captured(board[self.posnew])
			cap.capture()
			board[self.posnew] = self.name
			board[self.posold] = " _ "

class black_pawn(object):
	global board
	def __init__(self,posold,posnew,name):
		self.posold = posold
		self.posnew = posnew
		self.name = name
		
	def move(self):
		if self.posold == self.posnew + 8 and board[self.posnew] == " _ ":
			board[self.posold] = " _ "
			board[self.posnew] = self.name
		elif self.posold == self.posnew + 16 and board[self.posnew] == " _ ":
			for i in range(48,56):
				if self.posold == i:
					board[self.posold] = " _ "
					board[self.posnew] = self.name
		elif (self.posold == self.posnew + 7 and board[self.posnew] != " _ ") or (self.posold == self.posnew + 9 and board[self.posnew] != " _ " and 'b' not in board[self.posnew]):
			cap = captured(board[self.posnew])
			cap.capture()
			board[self.posnew] = self.name
			board[self.posold] = " _ "
			
while game == True:

	os.system('cls')
	show()
	pick = raw_input("Choose piece to move: ")
	pick = translate(pick)
	if 'wP' in board[pick] or 'bP' in board[pick]:
		for i in range(1,9):
			if board[pick] == "wP" + str(i):
				move = raw_input(pickt)
				if move == "":
					continue
				move = translate(move)
				wp1 = white_pawn(pick,move,board[pick])
				wp1.move()
			elif board[pick] == "bP" + str(i):
				move = raw_input(pickt)
				if move == "":
					continue
				move = translate(move)
				bp1 = black_pawn(pick,move,board[pick])
				bp1.move()
	elif board[pick] == 'bKI' or board[pick] == 'wKI':
		move = raw_input(pickt)
		if move == "":
			continue
		move = translate(move)
		king = pking(pick,move,board[pick])
		king.move()			
	elif 'bK' in board[pick] or 'wK' in board[pick]:
		move = raw_input(pickt)
		if move == "":
			continue
		move = translate(move)
		knight = pknight(pick,move,board[pick])
		knight.move()
	elif 'bB' in board[pick] or 'wB' in board[pick]:
		move = raw_input(pickt)
		if move == "":
			continue
		move = translate(move)
		bishop = pbishop(pick,move,board[pick])
		bishop.move()
	elif 'bR' in board[pick] or 'wR' in board[pick]:
		move = raw_input(pickt)
		if move == "":
			continue
		move = translate(move)
		rook = prook(pick,move,board[pick])
		rook.move()
	elif 'bQ' in board[pick] or 'wQ' in board[pick]:
		move = raw_input(pickt)
		if move == "":
			continue
		move = translate(move)
		queen = pqueen(pick,move,board[pick])
		queen.move()
	for i in range(8):
		if 'bP' in board[i]:
			revive("black",i,board[i])
	for i in range(56,64):
		if 'wP' in board[i]:
			revive("white",i,board[i])
	if 'wKI' in white_captured or 'bKI' in black_captured:
		exit()
