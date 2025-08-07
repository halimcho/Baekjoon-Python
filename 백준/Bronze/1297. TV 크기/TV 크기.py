D, H, W = map(int, input().split())

x = (D * D / (H * H + W * W)) ** 0.5

height = int(x * H)
width = int(x * W)

print(height, width)