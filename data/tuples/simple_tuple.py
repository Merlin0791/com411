def likelihood():
  likelihoods = (50, 38, 27, 99, 4)
  return min(likelihoods)

def run():
  print(f"\nMinimum likelihood of falling: {likelihood()}%\n")

run()