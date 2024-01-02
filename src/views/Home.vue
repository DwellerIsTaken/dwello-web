<script setup>
  import NavBar from "../components/NavBar.vue";
  import Footer from "../components/Footer.vue";
  import { ref, onMounted, onBeforeUnmount } from "vue";
  import { usePotiah, ScrollView, ScrollComponent } from "potiah";

  const flag = ref(true);
  const duration = ref(1.4);

  const discordIcon = "https://www.svgrepo.com/show/353655/discord-icon.svg";

</script>

<template>
  <main>
    <ScrollView :duration="duration" css-direction root>
      <div class="main mb-footer"> <!-- use mb-footer if you want to see footer-->
        <div class="w-col"></div>
          <div class="center">
            <NavBar />
            <div class="py-96 flex flex-col items-center justify-center text-[7.3rem] leading-none opacity-100 animate-fadeup">
              <h1 class="font-kanit ">Looking for a cool Discord Bot? <a class="underline text-[#007BFF] decoration-white selection:decoration-white" href="#">Invite me</a></h1>
              <!--somehow add a newline when screen gets too wide in order to keep second sentence on a new line.-->
              <!--when selecting the black background can overlap some of the selected text above; at least for big headers.-->
            </div>
            <div class="w-full flex relative z-10" :style="{ opacity: calculatedOpacity }">
              <div class="left">
                <h1 class="text-8xl mb-20">Hey, there</h1>
                <p class="mb-20">
                  Hello there! I'm Dwello, the newest addition to your Discord community. Ready to bring some cool features to your server and make it an even better place for everyone. Let's get started!
                </p>
                <div class="flex justify-between gap-5">
                  <div class="relative fillet">
                    <a href="#" class="text-xl p-4 pl-16 mt-8 rounded-full border-4 border-solid border-[#99aab5] bg-[#5965f2] text-white flex relative transition-transform duration-700 hover:">Add Dwello</a>
                    <div class="absolute top-[3.2rem] left-6">
                      <svg width="30px" height="30px" viewBox="0 -28.5 256 256" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" preserveAspectRatio="xMidYMid" fill="#000000">
                        <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
                        <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
                        <g id="SVGRepo_iconCarrier"> <g> <path d="M216.856339,16.5966031 C200.285002,8.84328665 182.566144,3.2084988 164.041564,0 C161.766523,4.11318106 159.108624,9.64549908 157.276099,14.0464379 C137.583995,11.0849896 118.072967,11.0849896 98.7430163,14.0464379 C96.9108417,9.64549908 94.1925838,4.11318106 91.8971895,0 C73.3526068,3.2084988 55.6133949,8.86399117 39.0420583,16.6376612 C5.61752293,67.146514 -3.4433191,116.400813 1.08711069,164.955721 C23.2560196,181.510915 44.7403634,191.567697 65.8621325,198.148576 C71.0772151,190.971126 75.7283628,183.341335 79.7352139,175.300261 C72.104019,172.400575 64.7949724,168.822202 57.8887866,164.667963 C59.7209612,163.310589 61.5131304,161.891452 63.2445898,160.431257 C105.36741,180.133187 151.134928,180.133187 192.754523,160.431257 C194.506336,161.891452 196.298154,163.310589 198.110326,164.667963 C191.183787,168.842556 183.854737,172.420929 176.223542,175.320965 C180.230393,183.341335 184.861538,190.991831 190.096624,198.16893 C211.238746,191.588051 232.743023,181.531619 254.911949,164.955721 C260.227747,108.668201 245.831087,59.8662432 216.856339,16.5966031 Z M85.4738752,135.09489 C72.8290281,135.09489 62.4592217,123.290155 62.4592217,108.914901 C62.4592217,94.5396472 72.607595,82.7145587 85.4738752,82.7145587 C98.3405064,82.7145587 108.709962,94.5189427 108.488529,108.914901 C108.508531,123.290155 98.3405064,135.09489 85.4738752,135.09489 Z M170.525237,135.09489 C157.88039,135.09489 147.510584,123.290155 147.510584,108.914901 C147.510584,94.5396472 157.658606,82.7145587 170.525237,82.7145587 C183.391518,82.7145587 193.761324,94.5189427 193.539891,108.914901 C193.539891,123.290155 183.391518,135.09489 170.525237,135.09489 Z" fill="#FFFFFF" fill-rule="nonzero"> 
                        </path> </g> </g>
                      </svg>
                    </div>
                  </div>
                  <a href="#" class="text-xl p-4 mt-8 rounded-full border-4 border-solid border-[#99aab5] text-white flex relative transition-colors duration-300 hover:bg-[#007BFF] hover:border-[#007BFF]">Login to Dashboard</a>
                </div>
              </div>
              <div class="right-center">
                <img
                  class="mt-7"
                  src="https://picsum.photos/seed/picsum/500/500"
                  alt="Discord Logo"
                  width="500"
                  height="500"
                />
              </div>
            </div>
            <div class="w-full flex relative z-20" data-scroll data-scroll-speed="0.3" :data-flag="flag">
              <div class="left">
                <h1 class="text-8xl mb-6">Invite me, please.</h1>
                <p>
                  Exciting news, Discord enthusiasts! Meet Dwello – your server's new
                  dynamic companion, ready to revolutionize your Discord adventures.
                  Dwello isn't just your typical bot; think of it as a
                  hyper-energetic, tech-savvy sidekick with lightning-fast responses,
                  rivaling a cheetah on a caffeine rush! We're so thrilled about this
                  launch that our coffee mugs are getting more attention than our
                  inboxes. But that's not all – Dwello boasts features so fantastic
                  they make unicorns jealous, from meme-tastic commands to server
                  management magic. Now, we're not just here to brag; we need your
                  help to spread the joy Picture Dwello as the friend always up for a
                  good time, and all we ask is for you to invite this digital dynamo
                  to your server. Your support means the world, and Dwello promises to
                  transform your server into the coolest spot in the Discord universe.
                  So, what are you waiting for? Let's turn those servers into
                  Dwello-icious hotspots together!
                </p>
                <div class="flex justify-between gap-5">
                  <a href="#" class="text-4xl p-4 mt-8 rounded-full border-4 border-solid border-black flex relative transition-transform duration-700 hover:scale-105">Invite to the server</a>
                  <a href="#" class="text-4xl p-4 mt-8 rounded border-4 border-solid border-black flex relative transition-transform duration-700 hover:scale-105">See features</a>
                </div>
              </div>
              <div class="right-center">
                <img
                  class="mt-7"
                  src="/src/assets/discord.svg"
                  alt="Discord Logo"
                  width="500"
                  height="500"
                />
              </div>
            </div>
          </div>
        <div class="w-col"></div>
      </div>
      <Footer />
    </ScrollView>
  </main>
</template>

<style scoped>
  .fillet {
    fill: #5965f2;
  }
</style>

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

      const distanceFromMiddle = Math.abs(scrollPosition - middleY);

      // Adjust the opacity based on the distance from the middle
      this.calculatedOpacity = 1 - distanceFromMiddle / 500;
    },
  },
};
</script>