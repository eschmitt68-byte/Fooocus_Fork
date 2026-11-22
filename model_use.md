# Model inventory

Inventory of every file currently under `models/`, including checkpoints, LoRAs, auxiliary model assets, configs, helper files, and placeholders.

**Total files: 181**

Preset usage is matched by filename against JSON files in `presets/`. `Not referenced` means no matching filename was found in those preset files; it does not indicate whether the file is loaded elsewhere by the application.

## Sampler and scheduler defaults

These are the `default_sampler` and `default_scheduler` values configured in each preset. Runtime settings or performance modes may override them.

| Preset | Sampler | Scheduler |
| --- | --- | --- |
| `presets/ChangedDress.json` | `dpmpp_2m_sde_gpu` | `karras` |
| `presets/ChangedDress_2.json` | `dpmpp_2m_sde_gpu` | `karras` |
| `presets/ChangedDress_3.json` | `dpmpp_2m_sde_gpu` | `karras` |
| `presets/ChangedDress_4.json` | `dpmpp_2m_sde_gpu` | `karras` |
| `presets/ChangedDress_5.json` | `dpmpp_2m_sde_gpu` | `karras` |
| `presets/ChangedDress_6.json` | `dpmpp_2m_sde_gpu` | `karras` |
| `presets/ChangedDress_7.json` | `dpmpp_2m_sde_gpu` | `karras` |
| `presets/ChangedDress_FlowerDress.json` | `dpmpp_2m_sde_gpu` | `karras` |
| `presets/Manga.json` | `dpmpp_2m_sde_gpu` | `karras` |
| `presets/anime.json` | `dpmpp_2m_sde_gpu` | `karras` |
| `presets/default.json` | `dpmpp_2m_sde_gpu` | `karras` |
| `presets/lcm.json` | `dpmpp_2m_sde_gpu` | `karras` |
| `presets/lightning.json` | `dpmpp_2m_sde_gpu` | `karras` |
| `presets/playground_v2.5.json` | `dpmpp_2m` | `edm_playground_v2.5` |
| `presets/pony_v6.json` | `dpmpp_2m_sde_gpu` | `karras` |
| `presets/realistic.json` | `dpmpp_2m_sde_gpu` | `karras` |
| `presets/sai.json` | `dpmpp_2m_sde_gpu` | `karras` |

## `checkpoints/` (5 files)

- `checkpoints/animaPencilXL_v500.safetensors` | Presets: `presets/anime.json` | Size: 6.46 GiB
- `checkpoints/juggernautXL_v8Rundiffusion.safetensors` | Presets: `presets/default.json`, `presets/lcm.json`, `presets/lightning.json` | Size: 6.62 GiB
- `checkpoints/photoMomentumSDXLNSFW_v20.safetensors` | Presets: `presets/ChangedDress.json`, `presets/ChangedDress_2.json`, `presets/ChangedDress_3.json`, `presets/ChangedDress_4.json`, `presets/ChangedDress_5.json`, `presets/ChangedDress_6.json`, `presets/ChangedDress_7.json`, `presets/ChangedDress_FlowerDress.json` | Size: 6.62 GiB
- `checkpoints/put_checkpoints_here` | Presets: Not referenced in any preset | Size: 0 B
- `checkpoints/realisticVisionV60B1_v51HyperVAE (1).safetensors` | Presets: `presets/ChangedDress.json`, `presets/ChangedDress_2.json`, `presets/ChangedDress_3.json`, `presets/ChangedDress_4.json`, `presets/ChangedDress_5.json`, `presets/ChangedDress_6.json`, `presets/ChangedDress_7.json`, `presets/ChangedDress_FlowerDress.json` | Size: 1.99 GiB

## `clip/` (1 files)

- `clip/put_clip_or_text_encoder_models_here` | Presets: Not referenced in any preset | Size: 0 B

## `clip_vision/` (4 files)

- `clip_vision/clip_vision_vit_h.safetensors` | Presets: Not referenced in any preset | Size: 1.84 GiB
- `clip_vision/model_base_caption_capfilt_large.pth` | Presets: Not referenced in any preset | Size: 854.57 MiB
- `clip_vision/put_clip_vision_models_here` | Presets: Not referenced in any preset | Size: 0 B
- `clip_vision/wd-v1-4-moat-tagger-v2.csv` | Presets: Not referenced in any preset | Size: 256.83 KiB

## `configs/` (11 files)

- `configs/anything_v3.yaml` | Presets: Not referenced in any preset | Size: 1.96 KiB
- `configs/v1-inference.yaml` | Presets: Not referenced in any preset | Size: 1.90 KiB
- `configs/v1-inference_clip_skip_2.yaml` | Presets: Not referenced in any preset | Size: 1.96 KiB
- `configs/v1-inference_clip_skip_2_fp16.yaml` | Presets: Not referenced in any preset | Size: 1.98 KiB
- `configs/v1-inference_fp16.yaml` | Presets: Not referenced in any preset | Size: 1.92 KiB
- `configs/v1-inpainting-inference.yaml` | Presets: Not referenced in any preset | Size: 2.01 KiB
- `configs/v2-inference-v.yaml` | Presets: Not referenced in any preset | Size: 1.84 KiB
- `configs/v2-inference-v_fp32.yaml` | Presets: Not referenced in any preset | Size: 1.84 KiB
- `configs/v2-inference.yaml` | Presets: Not referenced in any preset | Size: 1.81 KiB
- `configs/v2-inference_fp32.yaml` | Presets: Not referenced in any preset | Size: 1.81 KiB
- `configs/v2-inpainting-inference.yaml` | Presets: Not referenced in any preset | Size: 4.50 KiB

## `controlnet/` (8 files)

- `controlnet/control-lora-canny-rank128.safetensors` | Presets: Not referenced in any preset | Size: 377.40 MiB
- `controlnet/detection_Resnet50_Final.pth` | Presets: Not referenced in any preset | Size: 104.43 MiB
- `controlnet/fooocus_ip_negative.safetensors` | Presets: Not referenced in any preset | Size: 64.08 KiB
- `controlnet/fooocus_xl_cpds_128.safetensors` | Presets: Not referenced in any preset | Size: 377.38 MiB
- `controlnet/ip-adapter-plus-face_sdxl_vit-h.bin` | Presets: Not referenced in any preset | Size: 966.51 MiB
- `controlnet/ip-adapter-plus_sdxl_vit-h.bin` | Presets: Not referenced in any preset | Size: 966.51 MiB
- `controlnet/parsing_parsenet.pth` | Presets: Not referenced in any preset | Size: 81.38 MiB
- `controlnet/put_controlnets_and_t2i_here` | Presets: Not referenced in any preset | Size: 0 B

## `diffusers/` (1 files)

- `diffusers/put_diffusers_models_here` | Presets: Not referenced in any preset | Size: 0 B

## `embeddings/` (2 files)

- `embeddings/put_embeddings_or_textual_inversion_concepts_here` | Presets: Not referenced in any preset | Size: 0 B
- `embeddings/unaestheticXLv31.safetensors` | Presets: Not referenced in any preset | Size: 32.52 KiB

## `gligen/` (1 files)

- `gligen/put_gligen_models_here` | Presets: Not referenced in any preset | Size: 0 B

## `hypernetworks/` (1 files)

- `hypernetworks/put_hypernetworks_here` | Presets: Not referenced in any preset | Size: 0 B

## `inpaint/` (8 files)

- `inpaint/fooocus_inpaint_head.pth` | Presets: Not referenced in any preset | Size: 51.37 KiB
- `inpaint/inpaint_v26.fooocus.patch` | Presets: Not referenced in any preset | Size: 1.23 GiB
- `inpaint/isnet-general-use.onnx` | Presets: Not referenced in any preset | Size: 170.37 MiB
- `inpaint/put_inpaint_here` | Presets: Not referenced in any preset | Size: 0 B
- `inpaint/u2net.onnx` | Presets: Not referenced in any preset | Size: 167.84 MiB
- `inpaint/u2net_cloth_seg.onnx` | Presets: Not referenced in any preset | Size: 168.03 MiB
- `inpaint/u2net_human_seg.onnx` | Presets: Not referenced in any preset | Size: 167.84 MiB
- `inpaint/u2netp.onnx` | Presets: Not referenced in any preset | Size: 4.36 MiB

## `loras/` (119 files)

- `loras/Body_Adjusting Body Shape Slider from Lean to Full.figuration_V 1.0.safetensors` | Presets: Not referenced in any preset | Size: 51.83 MiB
- `loras/Body_barbie fy.safetensors` | Presets: `presets/ChangedDress.json` | Size: 81.47 MiB
- `loras/Body_bboobs-000005.safetensors` | Presets: `presets/ChangedDress.json`, `presets/ChangedDress_6.json`, `presets/ChangedDress_7.json` | Size: 109.14 MiB
- `loras/Body_BetterFaces-LoRA_v1.safetensors` | Presets: Not referenced in any preset | Size: 217.87 MiB
- `loras/Body_big-boobs-clothed-v2.safetensors` | Presets: `presets/ChangedDress_6.json`, `presets/ChangedDress_7.json` | Size: 37.92 MiB
- `loras/Body_Chubby__Chubby BBW - XL.safetensors` | Presets: Not referenced in any preset | Size: 507.44 MiB
- `loras/body_Chubby_a woman with balloons__in_bboobs-000005.safetensors` | Presets: `presets/ChangedDress_6.json`, `presets/ChangedDress_7.json` | Size: 109.14 MiB
- `loras/Body_Cubby_chubbyladyXL2.0.safetensors` | Presets: Not referenced in any preset | Size: 217.87 MiB
- `loras/Body_edgSexyAttireSDXLv1.safetensors` | Presets: Not referenced in any preset | Size: 27.57 MiB
- `loras/Body_Face_org4smic_sdxl.safetensors` | Presets: Not referenced in any preset | Size: 217.87 MiB
- `loras/Body_girlFace_Mila_XL.safetensors` | Presets: `presets/ChangedDress_2.json` | Size: 217.87 MiB
- `loras/Body_huge boobs_zsa-boobs-bonesBoobs_and_bones_ZIT_V1 (1).safetensors` | Presets: `presets/ChangedDress_2.json`, `presets/ChangedDress_3.json`, `presets/ChangedDress_4.json`, `presets/ChangedDress_5.json` | Size: 162.25 MiB
- `loras/Body_Muscle_Bimbo_SDXL (1).safetensors` | Presets: `presets/ChangedDress_2.json`, `presets/ChangedDress_3.json`, `presets/ChangedDress_4.json`, `presets/ChangedDress_5.json`, `presets/ChangedDress_6.json`, `presets/ChangedDress_7.json` | Size: 217.87 MiB
- `loras/Body_muscles_SDXL.safetensors` | Presets: Not referenced in any preset | Size: 217.88 MiB
- `loras/Body_natural breasts_epoch_5.safetensors` | Presets: Not referenced in any preset | Size: 217.87 MiB
- `loras/Body_niceCurvy_TH1N8U5TY LMBS_ThinBusty_SDXL_v2.safetensors` | Presets: `presets/ChangedDress_2.json`, `presets/ChangedDress_FlowerDress.json` | Size: 188.85 MiB
- `loras/Body_nude_SDXL_Sevenof9_7th_NSFW.safetensors` | Presets: Not referenced in any preset | Size: 649.67 MiB
- `loras/body_Penis_airoticart_penflac-penerec-1-LORA.safetensors` | Presets: Not referenced in any preset | Size: 144.11 MiB
- `loras/Body_Penis_asshole kotos.safetensors` | Presets: Not referenced in any preset | Size: 144.11 MiB
- `loras/Body_PerfectPussy_newb-000002.safetensors` | Presets: Not referenced in any preset | Size: 36.11 MiB
- `loras/Body_Portrait_1000_Girl_Faces.safetensors` | Presets: Not referenced in any preset | Size: 217.88 MiB
- `loras/Body_Pussy_airoticart_vulvdet1-LORA.safetensors` | Presets: Not referenced in any preset | Size: 144.11 MiB
- `loras/Body_Pussy_innievag.safetensors` | Presets: Not referenced in any preset | Size: 144.11 MiB
- `loras/Body_PussyAndAsshole_UberVag_LORA_V1.0.safetensors` | Presets: Not referenced in any preset | Size: 144.11 MiB
- `loras/Body_Tattoo_Test-000002.safetensors` | Presets: Not referenced in any preset | Size: 217.87 MiB
- `loras/Dres_Domina_0285 pink bodysuit_v1.safetensors` | Presets: Not referenced in any preset | Size: 72.11 MiB
- `loras/Dress_ catholicschooluniform.safetensors` | Presets: `presets/ChangedDress_5.json` | Size: 103.61 MiB
- `loras/Dress_ Cosplay_FemBisonCammy.safetensors` | Presets: Not referenced in any preset | Size: 9.11 MiB
- `loras/Dress_0223 flower_v1.safetensors` | Presets: `presets/ChangedDress_FlowerDress.json` | Size: 72.11 MiB
- `loras/Dress__Cyber_Hot.safetensors` | Presets: Not referenced in any preset | Size: 217.87 MiB
- `loras/Dress_Add_Details_v1.2.safetensors` | Presets: `presets/ChangedDress.json` | Size: 5.20 MiB
- `loras/Dress_amateur_style_v1_pony.safetensors` | Presets: Not referenced in any preset | Size: 2.66 MiB
- `loras/Dress_Bodycon_Shortdress_b0dyc0n1 (1).safetensors` | Presets: Not referenced in any preset | Size: 18.11 MiB
- `loras/Dress_boots.safetensors` | Presets: `presets/ChangedDress_4.json` | Size: 217.87 MiB
- `loras/Dress_Brasileira.safetensors` | Presets: Not referenced in any preset | Size: 217.88 MiB
- `loras/Dress_cameltoe_V2.1.safetensors` | Presets: Not referenced in any preset | Size: 144.11 MiB
- `loras/Dress_Cleopatre.safetensors` | Presets: `presets/ChangedDress_FlowerDress.json` | Size: 144.11 MiB
- `loras/Dress_Corset.safetensors` | Presets: `presets/ChangedDress_5.json` | Size: 72.12 MiB
- `loras/Dress_Cosplay_miku_cosplay_16thAnnDress_v1.safetensors` | Presets: Not referenced in any preset | Size: 144.12 MiB
- `loras/Dress_CrunchyBanana_cleavage_summer_dress.safetensors` | Presets: Not referenced in any preset | Size: 72.11 MiB
- `loras/Dress_Dimona dr3ss2dr3ss2.safetensors` | Presets: Not referenced in any preset | Size: 72.11 MiB
- `loras/Dress_Domina_b0dyc0n1_blue bodycon_dress.safetensors` | Presets: Not referenced in any preset | Size: 18.11 MiB
- `loras/Dress_Domina_Latex Fetish Dressm3shlat3x.safetensors` | Presets: Not referenced in any preset | Size: 9.11 MiB
- `loras/Dress_domina_latexbodysuitILL.safetensors` | Presets: `presets/ChangedDress_2.json` | Size: 217.87 MiB
- `loras/Dress_EveningDress_Real_Beauty.safetensors` | Presets: `presets/ChangedDress.json`, `presets/ChangedDress_4.json` | Size: 217.88 MiB
- `loras/Dress_FlowerDressSD15.safetensors` | Presets: Not referenced in any preset | Size: 69.37 MiB
- `loras/Dress_FlowerMeshDressILL.safetensors` | Presets: `presets/ChangedDress_FlowerDress.json` | Size: 217.87 MiB
- `loras/Dress_Golden Boy_MadamePresident_aiwaifu-10.safetensors` | Presets: Not referenced in any preset | Size: 36.13 MiB
- `loras/Dress_high-end_lingerie_b0ut1qu3.safetensors` | Presets: Not referenced in any preset | Size: 217.87 MiB
- `loras/Dress_High_Heels-000008.safetensors` | Presets: Not referenced in any preset | Size: 217.87 MiB
- `loras/Dress_JAY - BLUE FLOWER DRESS v2.safetensors` | Presets: Not referenced in any preset | Size: 144.11 MiB
- `loras/Dress_Ladies' sexy lingerie V2.0_v2.0.safetensors` | Presets: Not referenced in any preset | Size: 144.11 MiB
- `loras/Dress_latex_st4rtr3k_dress_red black blue light blue_star trek_gun_st4rtr3kXLP (1).safetensors` | Presets: Not referenced in any preset | Size: 217.87 MiB
- `loras/Dress_Latex_TankTop_Pants_By_Stable_Yogi.safetensors` | Presets: Not referenced in any preset | Size: 18.11 MiB
- `loras/Dress_lbc_pony_wedding dress_126-000006.safetensors` | Presets: Not referenced in any preset | Size: 109.13 MiB
- `loras/Dress_leather_dress_lora.TA_trained(3) (1).safetensors` | Presets: `presets/ChangedDress_2.json`, `presets/ChangedDress_3.json` | Size: 584.36 MiB
- `loras/Dress_Leather_Off-shoulder_Long_Dress_By_Stable_Yogi.safetensors` | Presets: Not referenced in any preset | Size: 18.11 MiB
- `loras/Dress_Leather_pants.safetensors` | Presets: Not referenced in any preset | Size: 217.87 MiB
- `loras/Dress_Leather_TankTop_Pants_By_Stable_Yogi.safetensors` | Presets: Not referenced in any preset | Size: 18.11 MiB
- `loras/Dress_leathertop.safetensors` | Presets: Not referenced in any preset | Size: 36.11 MiB
- `loras/Dress_Leopard Short Halter By Stable Yogi.safetensors` | Presets: Not referenced in any preset | Size: 36.11 MiB
- `loras/Dress_lingerieShop_L1ng3r13_st0r3.safetensors` | Presets: `presets/ChangedDress_4.json` | Size: 81.50 MiB
- `loras/Dress_Mistress_v4.safetensors` | Presets: Not referenced in any preset | Size: 217.87 MiB
- `loras/Dress_Nurse-08.safetensors` | Presets: Not referenced in any preset | Size: 36.12 MiB
- `loras/Dress_NurseSexy_Thai_nurse_uniform.safetensors` | Presets: Not referenced in any preset | Size: 36.12 MiB
- `loras/Dress_Off Shoulders Flower Print Dress By Stable Yogi.safetensors` | Presets: `presets/ChangedDress_FlowerDress.json` | Size: 36.11 MiB
- `loras/Dress_OnALeash-v2.safetensors` | Presets: Not referenced in any preset | Size: 144.11 MiB
- `loras/Dress_One-piece Swimsuit.safetensors` | Presets: Not referenced in any preset | Size: 144.11 MiB
- `loras/Dress_Plaid School Dress By Stable Yogi.safetensors` | Presets: Not referenced in any preset | Size: 36.11 MiB
- `loras/Dress_Playboy Magazine Model_Playboy Magazin.safetensors` | Presets: `presets/ChangedDress_3.json` | Size: 292.23 MiB
- `loras/Dress_quiron_HarleyQuinn_v1150_Lora.safetensors` | Presets: Not referenced in any preset | Size: 144.12 MiB
- `loras/Dress_robe_edgStraplessGlamourv1.safetensors` | Presets: Not referenced in any preset | Size: 18.11 MiB
- `loras/Dress_School Dress 2 By Stable Yogi.safetensors` | Presets: Not referenced in any preset | Size: 36.11 MiB
- `loras/Dress_Set.safetensors` | Presets: `presets/ChangedDress.json` | Size: 435.34 MiB
- `loras/Dress_sexy lingerie sheer dress_v1.0.safetensors` | Presets: Not referenced in any preset | Size: 144.11 MiB
- `loras/Dress_Sexy underwear for influencers with big eyes_v1.0.safetensors` | Presets: Not referenced in any preset | Size: 144.11 MiB
- `loras/Dress_Sexy_Womens__Steel_Boned_Corset_with_Zipper_SteampunkGothic.safetensors` | Presets: Not referenced in any preset | Size: 217.88 MiB
- `loras/Dress_Sexywhite lace sexy underwear_v1.0.safetensors` | Presets: Not referenced in any preset | Size: 144.11 MiB
- `loras/Dress_silverbodysuit_SevenOf9_SevensBodysuitQwen.safetensors` | Presets: Not referenced in any preset | Size: 140.85 MiB
- `loras/Dress_SpannishDress_edgLastRaysofSummer.safetensors` | Presets: Not referenced in any preset | Size: 36.11 MiB
- `loras/Dress_Special Forces Uniform - Tight Combat Suit_GK-sd-combat1.1.safetensors` | Presets: Not referenced in any preset | Size: 36.11 MiB
- `loras/Dress_Steampunk_Apparel_for_FLUX.safetensors` | Presets: Not referenced in any preset | Size: 217.87 MiB
- `loras/Dress_Steampunk_Butterfly.safetensors` | Presets: `presets/ChangedDress_6.json`, `presets/ChangedDress_7.json` | Size: 217.87 MiB
- `loras/Dress_SteampunkCorsetWithShrug.safetensors` | Presets: `presets/ChangedDress_6.json`, `presets/ChangedDress_7.json` | Size: 9.11 MiB
- `loras/Dress_SteampunkGoddessXL.safetensors` | Presets: Not referenced in any preset | Size: 217.87 MiB
- `loras/Dress_Summer_Dresses1.2.safetensors` | Presets: Not referenced in any preset | Size: 144.61 MiB
- `loras/Dress_SummerDresss_b_s_Jaq-17.safetensors` | Presets: Not referenced in any preset | Size: 18.11 MiB
- `loras/Dress_summerdressYellow.safetensors` | Presets: Not referenced in any preset | Size: 144.11 MiB
- `loras/Dress_white Sexy lingerie nude__NSFBSQQ.safetensors` | Presets: `presets/ChangedDress_5.json` | Size: 292.59 MiB
- `loras/exterior__Higwarts_Exterior-000015.safetensors` | Presets: Not referenced in any preset | Size: 36.11 MiB
- `loras/Face_Portrait_1000_Girl_Faces.safetensors` | Presets: Not referenced in any preset | Size: 217.88 MiB
- `loras/Face_SexyGirl_gonzalomoXLFluxPony_v60PhotoXLDMD.safetensors` | Presets: Not referenced in any preset | Size: 6.46 GiB
- `loras/General__ReaPhoLoRA.safetensors` | Presets: Not referenced in any preset | Size: 29.09 MiB
- `loras/Manga_1_Sexy long-legged beauty, Miss 199_1.0.safetensors` | Presets: Not referenced in any preset | Size: 72.11 MiB
- `loras/Manga_2_Muscle Mommy _ Goofy Ai_v1.0.safetensors` | Presets: `presets/Manga.json` | Size: 36.11 MiB
- `loras/Manga_Anime, cartoon, beautiful girl, sexy._v1.0.safetensors` | Presets: Not referenced in any preset | Size: 435.35 MiB
- `loras/Manga_Catwoman (DC Comics) Character Lora_v2.0.safetensors` | Presets: `presets/Manga.json` | Size: 36.14 MiB
- `loras/Manga_Kate Bishop _ Young Avengers _ Marvel Comics _  Commissioned _ ownwaifu_v1.0.safetensors` | Presets: `presets/Manga.json` | Size: 36.11 MiB
- `loras/Manga_PC Chan (dual char) _ Merryweather Comics_v1.0.safetensors` | Presets: Not referenced in any preset | Size: 18.11 MiB
- `loras/Manga_Pony XL & 1.5 Liliana anime Hentai_Pony XL.safetensors` | Presets: `presets/Manga.json` | Size: 27.58 MiB
- `loras/Manga_Pure quality - realistic large-breasted sexy goddess_1.0.safetensors` | Presets: `presets/Manga.json` | Size: 144.11 MiB
- `loras/Men_Handsome Spanish men_1.0.safetensors` | Presets: Not referenced in any preset | Size: 72.11 MiB
- `loras/Men_handsome_male-02.safetensors` | Presets: Not referenced in any preset | Size: 36.12 MiB
- `loras/Men_Y9RA0m_vKtCYIWpIVaDgn.safetensors` | Presets: Not referenced in any preset | Size: 36.11 MiB
- `loras/Pose_Deepthroat.safetensors` | Presets: Not referenced in any preset | Size: 9.11 MiB
- `loras/Pose_dildoRiding2-000005.safetensors` | Presets: Not referenced in any preset | Size: 9.17 MiB
- `loras/Pose_DoggystylePOV.safetensors` | Presets: Not referenced in any preset | Size: 144.11 MiB
- `loras/pose_FingerInsideXL.safetensors` | Presets: Not referenced in any preset | Size: 162.64 MiB
- `loras/Pose_MissionaryVaginal-v2.safetensors` | Presets: Not referenced in any preset | Size: 144.11 MiB
- `loras/Pose_orgasmFace_org4smic_sdxl.safetensors` | Presets: Not referenced in any preset | Size: 217.87 MiB
- `loras/Pose_PovDoggyAnal-v3.safetensors` | Presets: Not referenced in any preset | Size: 144.12 MiB
- `loras/Pose_Sexy Girl Hot Pose_Sexy Pose Asian.safetensors` | Presets: Not referenced in any preset | Size: 36.11 MiB
- `loras/Pose_Titfuck_Realistic.safetensors` | Presets: Not referenced in any preset | Size: 72.07 MiB
- `loras/Pose_toy_funtoys_v1.safetensors` | Presets: Not referenced in any preset | Size: 144.18 MiB
- `loras/put_loras_here` | Presets: Not referenced in any preset | Size: 0 B
- `loras/sd_xl_offset_example-lora_1.0.safetensors` | Presets: `presets/default.json`, `presets/sai.json` | Size: 47.26 MiB
- `loras/SDXL_FILM_PHOTOGRAPHY_STYLE_V1.safetensors` | Presets: `presets/realistic.json` | Size: 870.32 MiB
- `loras/sdxl_lcm_lora.safetensors` | Presets: Not referenced in any preset | Size: 375.61 MiB
- `loras/sdxl_lightning_4step_lora.safetensors` | Presets: Not referenced in any preset | Size: 375.61 MiB

## `prompt_expansion/` (9 files)

- `prompt_expansion/fooocus_expansion/config.json` | Presets: Not referenced in any preset | Size: 977 B
- `prompt_expansion/fooocus_expansion/merges.txt` | Presets: Not referenced in any preset | Size: 494.49 KiB
- `prompt_expansion/fooocus_expansion/positive.txt` | Presets: Not referenced in any preset | Size: 6.15 KiB
- `prompt_expansion/fooocus_expansion/pytorch_model.bin` | Presets: Not referenced in any preset | Size: 335.01 MiB
- `prompt_expansion/fooocus_expansion/special_tokens_map.json` | Presets: Not referenced in any preset | Size: 104 B
- `prompt_expansion/fooocus_expansion/tokenizer.json` | Presets: Not referenced in any preset | Size: 2.11 MiB
- `prompt_expansion/fooocus_expansion/tokenizer_config.json` | Presets: Not referenced in any preset | Size: 265 B
- `prompt_expansion/fooocus_expansion/vocab.json` | Presets: Not referenced in any preset | Size: 779.45 KiB
- `prompt_expansion/put_prompt_expansion_here` | Presets: Not referenced in any preset | Size: 0 B

## `safety_checker/` (1 files)

- `safety_checker/put_safety_checker_models_here` | Presets: Not referenced in any preset | Size: 0 B

## `style_models/` (1 files)

- `style_models/put_t2i_style_model_here` | Presets: Not referenced in any preset | Size: 0 B

## `unet/` (1 files)

- `unet/put_unet_files_here` | Presets: Not referenced in any preset | Size: 0 B

## `upscale_models/` (2 files)

- `upscale_models/fooocus_upscaler_s409985e5.bin` | Presets: Not referenced in any preset | Size: 32.08 MiB
- `upscale_models/put_esrgan_and_other_upscale_models_here` | Presets: Not referenced in any preset | Size: 0 B

## `vae/` (1 files)

- `vae/put_vae_here` | Presets: Not referenced in any preset | Size: 0 B

## `vae_approx/` (5 files)

- `vae_approx/put_taesd_encoder_pth_and_taesd_decoder_pth_here` | Presets: Not referenced in any preset | Size: 0 B
- `vae_approx/vaeapp_sd15.pth` | Presets: Not referenced in any preset | Size: 208.77 KiB
- `vae_approx/xl-to-v1_interposer-v3.1.safetensors` | Presets: Not referenced in any preset | Size: 6.25 MiB
- `vae_approx/xl-to-v1_interposer-v4.0.safetensors` | Presets: Not referenced in any preset | Size: 5.40 MiB
- `vae_approx/xlvaeapp.pth` | Presets: Not referenced in any preset | Size: 208.77 KiB
