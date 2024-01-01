class PyTableConsole:
    def __init__(self, contains = []):
        self.contains = contains
    def width(self):
        return len(self.contains)
    def update(self):
        max_height = 0
        i = 0
        while i < len(self.contains):
            current_height = 0
            if self.contains[i]:
                current_height = len(self.contains[i])
            
            if max_height < current_height:
                max_height = current_height
            i+=1
        i = 0
        while i < len(self.contains):
            current_height = 0
            if self.contains[i]:
                current_height = len(self.contains[i])
            if current_height < max_height:
                ii = current_height
                while ii < max_height:
                    self.contains[i].append("")
                    ii+=1
            i+=1
    def height(self):
        self.update()
        if self.contains:
            return len(self.contains[0])
        else:
            return 0
    def __str__(self):
        self.update()
        out_text = ""
        column_max_width = []
        i = 0
        while i < self.width():
            column_max_width.append(0)
            ii = 0
            while ii < self.height():
                if column_max_width[i] < len(str(self.contains[i][ii])):
                    column_max_width[i] = len(str(self.contains[i][ii]))
                ii+=1
            i+=1
        i = 0
        while i < self.height():
            ii = 0
            while ii < self.width():
                out_text += "|" + " "*(column_max_width[ii] - len(str(self.contains[ii][i]))) + str(self.contains[ii][i])
                ii+=1
            out_text+="|\n"
            i+=1
        return out_text
    