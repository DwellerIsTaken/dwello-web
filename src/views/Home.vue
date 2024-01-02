<script setup>
  import NavBar from "../components/NavBar.vue";
  import Footer from "../components/Footer.vue";
  import { ref, onMounted, onBeforeUnmount } from "vue";
  import { usePotiah, ScrollView, ScrollComponent } from "potiah";

  const flag = ref(true);
  const duration = ref(1.4);

</script>

<template>
  <main>
    <ScrollView :duration="duration" css-direction root>
      <div class="main mb-footer"> <!-- use mb-footer if you want to see footer-->
        <div class="w-col"></div>
          <div class="center">
            <NavBar />
            <div class="py-96 flex flex-col items-center justify-center text-[7.3rem] leading-none opacity-100 animate-fadeup">
              <h1 class="font-kanit ">Looking for a cool Discord Bot? <a class="underline text-blue decoration-white selection:decoration-white" href="#">Invite me</a></h1>
              <!--somehow add a newline when screen gets too wide in order to keep second sentence on a new line.-->
              <!--when selecting the black background can overlap some of the selected text above; at least for big headers.-->
            </div>
            <div class="w-full flex relative z-10" :style="{ opacity: calculatedOpacity }">
              <div class="left">
                <h1 class="text-8xl">Hey, there</h1>
                <p class="my-20">
                  Hello there! I'm Dwello, the newest addition to your Discord community. Ready to bring some cool features to your server and make it an even better place for everyone. Let's get started!
                </p>
                <div class="flex justify-between gap-5">
                  <a href="#">
                    <button class="bg-discord hover:text-discord group mt-8 flex items-center gap-3 rounded-full border-4 border-solid border-[#99aab5] p-4 text-xl font-bold text-white transition-colors duration-300 hover:bg-white hover:border-white">
                      <svg class="group-hover:fill-discord fill-white transition-colors duration-300" width="30px" height="30px" viewBox="0 -28.5 256 256" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" preserveAspectRatio="xMidYMid">
                        <path d="M216.856339,16.5966031 C200.285002,8.84328665 182.566144,3.2084988 164.041564,0 C161.766523,4.11318106 159.108624,9.64549908 157.276099,14.0464379 C137.583995,11.0849896 118.072967,11.0849896 98.7430163,14.0464379 C96.9108417,9.64549908 94.1925838,4.11318106 91.8971895,0 C73.3526068,3.2084988 55.6133949,8.86399117 39.0420583,16.6376612 C5.61752293,67.146514 -3.4433191,116.400813 1.08711069,164.955721 C23.2560196,181.510915 44.7403634,191.567697 65.8621325,198.148576 C71.0772151,190.971126 75.7283628,183.341335 79.7352139,175.300261 C72.104019,172.400575 64.7949724,168.822202 57.8887866,164.667963 C59.7209612,163.310589 61.5131304,161.891452 63.2445898,160.431257 C105.36741,180.133187 151.134928,180.133187 192.754523,160.431257 C194.506336,161.891452 196.298154,163.310589 198.110326,164.667963 C191.183787,168.842556 183.854737,172.420929 176.223542,175.320965 C180.230393,183.341335 184.861538,190.991831 190.096624,198.16893 C211.238746,191.588051 232.743023,181.531619 254.911949,164.955721 C260.227747,108.668201 245.831087,59.8662432 216.856339,16.5966031 Z M85.4738752,135.09489 C72.8290281,135.09489 62.4592217,123.290155 62.4592217,108.914901 C62.4592217,94.5396472 72.607595,82.7145587 85.4738752,82.7145587 C98.3405064,82.7145587 108.709962,94.5189427 108.488529,108.914901 C108.508531,123.290155 98.3405064,135.09489 85.4738752,135.09489 Z M170.525237,135.09489 C157.88039,135.09489 147.510584,123.290155 147.510584,108.914901 C147.510584,94.5396472 157.658606,82.7145587 170.525237,82.7145587 C183.391518,82.7145587 193.761324,94.5189427 193.539891,108.914901 C193.539891,123.290155 183.391518,135.09489 170.525237,135.09489 Z"></path>
                      </svg>
                      <span>Add Dwello</span>
                    </button>
                  </a>
                  <a href="#">
                    <button class="text-xl font-bold p-4 mt-8 rounded-full border-4 border-solid border-[#99aab5] text-white flex relative transition-colors duration-300 hover:bg-blue hover:border-blue">
                      <span>Login to Dashboard</span>
                    </button>
                  </a>
                </div>
              </div>
              <div class="right">
                <img
                  src="https://picsum.photos/seed/picsum/500/500"
                  alt="Some Image"
                  width="500"
                  height="500"
                />
              </div>
            </div>
            <div class="w-full flex relative z-20" data-scroll data-scroll-speed="0.3" :data-flag="flag">
              <div class="left">
                <img
                  src="https://picsum.photos/seed/picsum/500/500"
                  alt="Some Image"
                  width="500"
                  height="500"
                />
              </div>
              <div class="left">
                <h1 class="text-8xl mb-6">Customize your experience</h1>
                <p class="mt-20 mb-[3.25rem]">
                  Elevate your Discord experience with advanced customization options. Tailor outputs, fine-tune server settings, and take control of personal preferences, including the ability to disable intrusive bot DMs. Your Discord, your way – customize effortlessly!
                </p>
                <a href="#" class="text-blue">Learn More &#10230;</a>
              </div>
            </div>
            <div class="w-full flex relative z-30 -mt-32" data-scroll data-scroll-speed="0.6" :data-flag="flag">
              <div class="left">
                <h1 class="text-8xl">Economy & Market</h1>
                <p class="my-20">
                  Get ready for the Discord-wide party of trading! Jump into the action as you trade unique virtual goodies across servers, tweak trends, and play with prices. It's not just a market; it's an exhilarating global economy waiting for your moves!
                </p>
                <a href="#" class="text-blue">Learn More &#10230;</a>
              </div>
              <div class="right">
                <img
                  src="https://picsum.photos/seed/picsum/500/500"
                  alt="Some Image"
                  width="500"
                  height="500"
                />
              </div>
            </div>
            <div class="w-full flex relative z-40 -mt-52" data-scroll data-scroll-speed="0.9" :data-flag="flag">
              <div class="left">
                <img
                  src="https://picsum.photos/seed/picsum/500/500"
                  alt="Some Image"
                  width="500"
                  height="500"
                />
              </div>
              <div class="left">
                <h1 class="text-8xl mb-6">Levelling & Leaderboards</h1>
                <p class="mt-20 mb-12">
                  Level up across servers, snagging cool rewards and climbing leaderboards. And guess what? We've got the annoying notifications turned off by default, so you can enjoy the game without the buzzkill. Ready to dominate the leaderboards? Let the leveling adventure begin! 
                </p>
                <a href="#" class="text-blue">Learn More &#10230;</a>
              </div>
            </div>
            <div class="w-full flex relative z-50 -mt-72" data-scroll data-scroll-speed="1.2" :data-flag="flag">
              <div class="left">
                <h1 class="text-8xl">Moderation</h1>
                <p class="my-20">
                  Transform your Discord experience with cutting-edge moderation tools. Elevate control, manage content effortlessly, and create a thriving community where conversations flourish.
                </p>
                <a href="#" class="text-blue">Learn More &#10230;</a>
              </div>
              <div class="right">
                <img
                  src="https://picsum.photos/seed/picsum/500/500"
                  alt="Some Image"
                  width="500"
                  height="500"
                />
              </div>
            </div>
            <div class="w-full flex relative z-[60] mt-[-18rem]" data-scroll data-scroll-speed="1.5" :data-flag="flag">
              <div class="left">
                <img
                  src="https://picsum.photos/seed/picsum/500/500"
                  alt="Some Image"
                  width="500"
                  height="500"
                />
              </div>
              <div class="left">
                <h1 class="text-8xl mb-6">Other Features</h1>
                <p class="mt-20 mb-12">
                  Unlock a world of possibilities with additional features. From managing to-do lists seamlessly to accessing dynamic API-based commands for movie, weather, and track information, our utility commands empower your Discord server with versatility and convenience. Enhance every interaction and make your community truly extraordinary.
                </p>
                <a href="#" class="text-blue">Learn More &#10230;</a>
              </div>
            </div>
          </div>
        <div class="w-col"></div>
      </div>
      <Footer />
    </ScrollView>
  </main>
</template>

<script>
export default {
  data() {
    return {
      calculatedOpacity: 0,
    };
  },
  mounted() {
    window.addEventListener("scroll", this.handleScroll);
  },
  beforeDestroy() {
    window.removeEventListener("scroll", this.handleScroll);
  },
  methods: {
    handleScroll() {
      const scrollPosition = window.scrollY;
      const middleY = window.innerHeight / 2;
      console.log(middleY);

      const distanceFromMiddle = Math.abs(scrollPosition - middleY);

      // Adjust the opacity based on the distance from the middle
      this.calculatedOpacity = 1 - distanceFromMiddle / 500;
    },
  },
};
</script>