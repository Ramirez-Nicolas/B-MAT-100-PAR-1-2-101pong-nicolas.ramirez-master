##
## EPITECH PROJECT, 2020
## Makefile
## File description:
## makefile
##

SRC = 101pong.py 

NAME = 101pong

OBJ = $(SRC)

$(NAME) : $(OBJ)
	cp $(OBJ) $(NAME)
	chmod +x $(NAME)
