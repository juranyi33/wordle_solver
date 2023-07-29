from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from evaluators.evaluator import EvaluatorBase
from solver import Solver

wordle_path = 'https://www.nytimes.com/games/wordle/index.html'
PATH = "C:\Program Files (x86)\chromedriver.exe"
opt = Options()
opt.add_experimental_option("debuggerAddress", "localhost:8989")
driver = webdriver.Chrome(executable_path=PATH, chrome_options=opt)

evaluator = EvaluatorBase("possible_words.txt")

solver = Solver(driver=driver, evaluator=evaluator, wordle_path=wordle_path)

if __name__ == "__main__":
    solver.solve()
