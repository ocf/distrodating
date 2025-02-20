base_url="https://www.ocf.berkeley.edu/~ronitnath/distrod/distrodating-1.0-web/game/images/"
output_dir="game/images"

mkdir -p $output_dir

files=(
    "arch_hub.webp"
    "debian_center.webp"
    "fedora_lounge.webp"
    "mint_cafe.webp"
    "terminal_festival.webp"
    "ubuntu_pavilion.webp"
)

for file in "${files[@]}"; do
    curl -o "$output_dir/$file" "$base_url$file"
done
