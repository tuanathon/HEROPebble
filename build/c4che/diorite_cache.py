AR = 'arm-none-eabi-ar'
ARFLAGS = 'rcs'
AS = 'arm-none-eabi-gcc'
BINDIR = '/usr/local/bin'
BLOCK_MESSAGE_KEYS = []
BUILD_DIR = 'diorite'
BUILD_TYPE = 'app'
BUNDLE_BIN_DIR = 'diorite'
BUNDLE_NAME = 'GoProJS.pbw'
CC = ['arm-none-eabi-gcc']
CCLNK_SRC_F = []
CCLNK_TGT_F = ['-o']
CC_NAME = 'gcc'
CC_SRC_F = []
CC_TGT_F = ['-c', '-o']
CC_VERSION = ('6', '3', '0')
CFLAGS = ['-std=c99', '-mcpu=cortex-m3', '-mthumb', '-ffunction-sections', '-fdata-sections', '-g', '-fPIE', '-Os', '-D_TIME_H_', '-Wall', '-Wextra', '-Werror', '-Wno-unused-parameter', '-Wno-error=unused-function', '-Wno-error=unused-variable']
CFLAGS_MACBUNDLE = ['-fPIC']
CFLAGS_cshlib = ['-fPIC']
CPPPATH_ST = '-I%s'
DEFINES = ['RELEASE', 'PBL_PLATFORM_DIORITE', 'PBL_BW', 'PBL_RECT', 'PBL_MICROPHONE', 'PBL_HEALTH', 'PBL_SMARTSTRAP', 'PBL_DISPLAY_WIDTH=144', 'PBL_DISPLAY_HEIGHT=168', 'PBL_SDK_3']
DEFINES_ST = '-D%s'
DEST_BINFMT = 'elf'
DEST_CPU = 'arm'
DEST_OS = 'linux'
INCLUDES = ['diorite']
LD = 'arm-none-eabi-ld'
LIBDIR = '/usr/local/lib'
LIBPATH_ST = '-L%s'
LIB_DIR = 'node_modules'
LIB_JSON = [{u'gitHead': u'946675bdadff2064131a7eeca84b3a2bdd48e7a4', u'_location': u'/pebblejs', u'dist': {u'tarball': u'https://registry.npmjs.org/pebblejs/-/pebblejs-1.0.0.tgz', u'shasum': u'ddf31286fdda533a159a083b9ad2cb2ea8198e8c'}, u'_spec': u'pebblejs', u'_npmOperationalInternal': {u'tmp': u'tmp/pebblejs-1.0.0.tgz_1482176387800_0.8418819417711347', u'host': u'packages-18-east.internal.npmjs.com'}, u'keywords': [u'pebble-package'], u'devDependencies': {u'coffee-script': u'^1.11.1'}, u'_from': u'pebblejs@latest', u'pebble': {u'sdkVersion': u'3', u'resources': {u'media': [{u'menuIcon': True, u'type': u'bitmap', u'name': u'SIMPLY_IMAGE_MENU_ICON', u'file': u'images/menu_icon.png'}, {u'type': u'bitmap', u'name': u'SIMPLY_IMAGE_LOGO_SPLASH', u'file': u'images/logo_splash.png'}, {u'type': u'bitmap', u'name': u'SIMPLY_IMAGE_TILE_SPLASH', u'file': u'images/tile_splash.png'}, {u'type': u'font', u'name': u'SIMPLY_MONO_FONT_14', u'file': u'fonts/UbuntuMono-Regular.ttf'}]}, u'projectType': u'package', u'targetPlatforms': [u'aplite', u'basalt', u'chalk', u'diorite'], u'capabilities': [u'configurable']}, u'_inCache': True, u'_phantomChildren': {}, u'_args': [[{u'name': u'pebblejs', u'escapedName': u'pebblejs', u'rawSpec': u'', u'raw': u'pebblejs', u'scope': None, u'type': u'tag', u'spec': u'latest'}, u'/home/konrad/Pebble Projects/GoProJS']], u'_nodeVersion': u'7.2.1', u'version': u'1.0.0', u'_resolved': u'https://registry.npmjs.org/pebblejs/-/pebblejs-1.0.0.tgz', u'readme': u'ERROR: No README data found!', u'homepage': u'https://github.com/pebble/pebblejs#readme', u'files': [u'dist.zip'], u'_npmVersion': u'3.10.9', u'_requested': {u'name': u'pebblejs', u'escapedName': u'pebblejs', u'rawSpec': u'', u'raw': u'pebblejs', u'scope': None, u'type': u'tag', u'spec': u'latest'}, u'description': u'Pebble.js =========', u'repository': {u'url': u'git+https://github.com/pebble/pebblejs.git', u'type': u'git'}, u'optionalDependencies': {}, u'_requiredBy': [u'#USER', u'/'], u'maintainers': [{u'name': u'pebble-tech', u'email': u'webteam@getpebble.com'}], u'dependencies': {}, u'scripts': {}, 'path': 'node_modules/pebblejs/dist', u'_shrinkwrap': None, u'name': u'pebblejs', u'license': u'MIT', u'directories': {}, u'author': {u'name': u'Meiguro'}, u'bugs': {u'url': u'https://github.com/pebble/pebblejs/issues'}, u'_npmUser': {u'name': u'pebble-tech', u'email': u'webteam@getpebble.com'}, 'js_paths': ['node_modules/pebblejs/dist/js/clock/clock.js', 'node_modules/pebblejs/dist/js/clock/index.js', 'node_modules/pebblejs/dist/js/index.js', 'node_modules/pebblejs/dist/js/lib/ajax.js', 'node_modules/pebblejs/dist/js/lib/color.js', 'node_modules/pebblejs/dist/js/lib/emitter.js', 'node_modules/pebblejs/dist/js/lib/image.js', 'node_modules/pebblejs/dist/js/lib/myutil.js', 'node_modules/pebblejs/dist/js/lib/png-encoder.js', 'node_modules/pebblejs/dist/js/lib/struct.js', 'node_modules/pebblejs/dist/js/lib/util2.js', 'node_modules/pebblejs/dist/js/lib/vector2.js', 'node_modules/pebblejs/dist/js/platform/feature.js', 'node_modules/pebblejs/dist/js/platform/index.js', 'node_modules/pebblejs/dist/js/platform/platform.js', 'node_modules/pebblejs/dist/js/settings/index.js', 'node_modules/pebblejs/dist/js/settings/settings.js', 'node_modules/pebblejs/dist/js/simply/simply.js', 'node_modules/pebblejs/dist/js/smartpackage/package-pebble.js', 'node_modules/pebblejs/dist/js/smartpackage/package.js', 'node_modules/pebblejs/dist/js/timeline/index.js', 'node_modules/pebblejs/dist/js/timeline/timeline.js', 'node_modules/pebblejs/dist/js/ui/accel.js', 'node_modules/pebblejs/dist/js/ui/card.js', 'node_modules/pebblejs/dist/js/ui/circle.js', 'node_modules/pebblejs/dist/js/ui/element.js', 'node_modules/pebblejs/dist/js/ui/image.js', 'node_modules/pebblejs/dist/js/ui/imageservice.js', 'node_modules/pebblejs/dist/js/ui/index.js', 'node_modules/pebblejs/dist/js/ui/inverter.js', 'node_modules/pebblejs/dist/js/ui/light.js', 'node_modules/pebblejs/dist/js/ui/line.js', 'node_modules/pebblejs/dist/js/ui/menu.js', 'node_modules/pebblejs/dist/js/ui/propable.js', 'node_modules/pebblejs/dist/js/ui/radial.js', 'node_modules/pebblejs/dist/js/ui/rect.js', 'node_modules/pebblejs/dist/js/ui/resource.js', 'node_modules/pebblejs/dist/js/ui/simply-pebble.js', 'node_modules/pebblejs/dist/js/ui/simply.js', 'node_modules/pebblejs/dist/js/ui/stage.js', 'node_modules/pebblejs/dist/js/ui/tests.js', 'node_modules/pebblejs/dist/js/ui/text.js', 'node_modules/pebblejs/dist/js/ui/timetext.js', 'node_modules/pebblejs/dist/js/ui/vibe.js', 'node_modules/pebblejs/dist/js/ui/voice.js', 'node_modules/pebblejs/dist/js/ui/window.js', 'node_modules/pebblejs/dist/js/ui/windowstack.js', 'node_modules/pebblejs/dist/js/vendor/moment.js', 'node_modules/pebblejs/dist/js/vendor/png.js', 'node_modules/pebblejs/dist/js/vendor/zlib.js', 'node_modules/pebblejs/dist/js/wakeup/index.js', 'node_modules/pebblejs/dist/js/wakeup/wakeup.js'], u'_where': u'/home/konrad/Pebble Projects/GoProJS', u'_id': u'pebblejs@1.0.0', u'_shasum': u'ddf31286fdda533a159a083b9ad2cb2ea8198e8c'}, {u'gitHead': u'1bf6db08092ab464974d1762a953ea7cbd24efb8', u'_location': u'/pebble-clay', u'dist': {u'tarball': u'https://registry.npmjs.org/pebble-clay/-/pebble-clay-1.0.4.tgz', u'shasum': u'fdf92f0fdc770a979c06874eaa2457cc2e762344'}, u'_spec': u'pebble-clay', u'_npmOperationalInternal': {u'tmp': u'tmp/pebble-clay-1.0.4.tgz_1479759281024_0.1520081793423742', u'host': u'packages-12-west.internal.npmjs.com'}, u'keywords': [u'pebble', u'config', u'configuration', u'pebble-package'], u'devDependencies': {u'chai': u'^3.4.1', u'mocha': u'^2.3.4', u'through': u'^2.3.8', u'gulp-inline': u'0.0.15', u'karma-source-map-support': u'^1.1.0', u'deepcopy': u'^0.6.1', u'eslint-plugin-standard': u'^1.3.1', u'stringify': u'^3.2.0', u'gulp-insert': u'^0.5.0', u'gulp': u'^3.9.0', u'gulp-htmlmin': u'^1.3.0', u'deamdify': u'^0.2.0', u'bourbon': u'^4.2.6', u'eslint-config-pebble': u'^1.2.0', u'eslint': u'^1.5.1', u'karma-coverage': u'^0.5.3', u'watchify': u'^3.7.0', u'require-from-string': u'^1.1.0', u'gulp-sourcemaps': u'^1.6.0', u'karma-mocha': u'^0.2.1', u'sinon': u'^1.17.3', u'joi': u'^6.10.1', u'browserify': u'^13.0.0', u'sassify': u'^0.9.1', u'gulp-autoprefixer': u'^3.1.0', u'karma-mocha-reporter': u'^1.1.5', u'autoprefixer': u'^6.3.1', u'browserify-istanbul': u'^0.2.1', u'karma-threshold-reporter': u'^0.1.15', u'gulp-sass': u'^2.1.1', u'vinyl-source-stream': u'^1.1.0', u'gulp-uglify': u'^1.5.2', u'karma-chrome-launcher': u'^0.2.2', u'vinyl-buffer': u'^1.0.0', u'del': u'^2.0.2', u'karma': u'^0.13.19', u'karma-browserify': u'^5.0.1', u'tosource': u'^1.0.0', u'postcss': u'^5.0.14'}, u'_from': u'pebble-clay@latest', u'pebble': {u'sdkVersion': u'3', u'capabilities': [u'configurable'], u'projectType': u'package', u'targetPlatforms': [u'aplite', u'basalt', u'chalk', u'diorite', u'emery'], u'resources': {u'media': []}}, u'_inCache': True, u'_phantomChildren': {}, u'_args': [[{u'name': u'pebble-clay', u'escapedName': u'pebble-clay', u'rawSpec': u'', u'raw': u'pebble-clay', u'scope': None, u'type': u'tag', u'spec': u'latest'}, u'/home/konrad/Pebble Projects/GoProJS']], u'_nodeVersion': u'6.9.1', u'version': u'1.0.4', u'_resolved': u'https://registry.npmjs.org/pebble-clay/-/pebble-clay-1.0.4.tgz', u'readme': u'ERROR: No README data found!', u'homepage': u'https://github.com/pebble/clay#readme', u'_npmVersion': u'3.10.8', u'_requested': {u'name': u'pebble-clay', u'escapedName': u'pebble-clay', u'rawSpec': u'', u'raw': u'pebble-clay', u'scope': None, u'type': u'tag', u'spec': u'latest'}, u'description': u'Pebble Config Framework', u'repository': {u'url': u'git+https://github.com/pebble/clay.git', u'type': u'git'}, u'optionalDependencies': {}, u'_requiredBy': [u'#USER', u'/'], u'maintainers': [{u'name': u'pebble-tech', u'email': u'webteam@getpebble.com'}], u'dependencies': {}, u'scripts': {u'pebble-publish': u'npm run pebble-clean && npm run build && pebble build && pebble package publish && npm run pebble-clean', u'test-travis': u'gulp && ./node_modules/.bin/karma start ./test/karma.conf.js --single-run --browsers chromeTravisCI && ./node_modules/.bin/eslint ./', u'pebble-build': u'npm run build && pebble build', u'test-debug': u'(export DEBUG=true && ./node_modules/.bin/gulp && ./node_modules/.bin/karma start ./test/karma.conf.js --no-single-run)', u'lint': u'eslint ./', u'dev': u'gulp dev', u'build': u'gulp', u'test': u'gulp && ./node_modules/.bin/karma start ./test/karma.conf.js --single-run', u'pebble-clean': u'rm -rf tmp src/js/index.js && pebble clean'}, 'path': 'node_modules/pebble-clay/dist', u'_shrinkwrap': None, u'name': u'pebble-clay', u'license': u'MIT', u'directories': {}, u'author': {u'name': u'Pebble Technology'}, u'bugs': {u'url': u'https://github.com/pebble/clay/issues'}, u'_npmUser': {u'name': u'pebble-tech', u'email': u'webteam@getpebble.com'}, 'js_paths': ['node_modules/pebble-clay/dist/js/index.js'], u'_where': u'/home/konrad/Pebble Projects/GoProJS', u'_id': u'pebble-clay@1.0.4', u'_shasum': u'fdf92f0fdc770a979c06874eaa2457cc2e762344'}]
LIB_RESOURCES_JSON = {u'pebblejs': [{u'menuIcon': True, u'type': u'bitmap', u'name': u'SIMPLY_IMAGE_MENU_ICON', u'file': u'images/menu_icon.png'}, {u'type': u'bitmap', u'name': u'SIMPLY_IMAGE_LOGO_SPLASH', u'file': u'images/logo_splash.png'}, {u'type': u'bitmap', u'name': u'SIMPLY_IMAGE_TILE_SPLASH', u'file': u'images/tile_splash.png'}, {u'type': u'font', u'name': u'SIMPLY_MONO_FONT_14', u'file': u'fonts/UbuntuMono-Regular.ttf'}], u'pebble-clay': []}
LIB_ST = '-l%s'
LINKFLAGS = ['-mcpu=cortex-m3', '-mthumb', '-Wl,--gc-sections', '-Wl,--warn-common', '-fPIE', '-Os']
LINKFLAGS_MACBUNDLE = ['-bundle', '-undefined', 'dynamic_lookup']
LINKFLAGS_cshlib = ['-shared']
LINKFLAGS_cstlib = ['-Wl,-Bstatic']
LINK_CC = ['arm-none-eabi-gcc']
MESSAGE_KEYS = {u'MESSAGE_KEY_refreshrate': 10001, u'MESSAGE_KEY_simplemode': 10000}
MESSAGE_KEYS_DEFINITION = '/home/konrad/Pebble Projects/GoProJS/build/src/message_keys.auto.c'
MESSAGE_KEYS_HEADER = '/home/konrad/Pebble Projects/GoProJS/build/include/message_keys.auto.h'
MESSAGE_KEYS_JSON = '/home/konrad/Pebble Projects/GoProJS/build/js/message_keys.json'
NODE_PATH = '/home/konrad/.pebble-sdk/SDKs/current/node_modules'
PEBBLE_SDK_COMMON = '/home/konrad/.pebble-sdk/SDKs/current/sdk-core/pebble/common'
PEBBLE_SDK_PLATFORM = '/home/konrad/.pebble-sdk/SDKs/current/sdk-core/pebble/diorite'
PEBBLE_SDK_ROOT = '/home/konrad/.pebble-sdk/SDKs/current/sdk-core/pebble'
PLATFORM = {'TAGS': ['diorite', 'bw', 'rect', 'mic', 'strap', 'health', '144w', '168h'], 'MAX_FONT_GLYPH_SIZE': 256, 'ADDITIONAL_TEXT_LINES_FOR_PEBBLE_H': [], 'MAX_APP_BINARY_SIZE': 65536, 'MAX_RESOURCES_SIZE': 1048576, 'MAX_APP_MEMORY_SIZE': 65536, 'MAX_WORKER_MEMORY_SIZE': 10240, 'NAME': 'diorite', 'BUNDLE_BIN_DIR': 'diorite', 'BUILD_DIR': 'diorite', 'MAX_RESOURCES_SIZE_APPSTORE': 262144, 'DEFINES': ['PBL_PLATFORM_DIORITE', 'PBL_BW', 'PBL_RECT', 'PBL_MICROPHONE', 'PBL_HEALTH', 'PBL_SMARTSTRAP', 'PBL_DISPLAY_WIDTH=144', 'PBL_DISPLAY_HEIGHT=168']}
PLATFORM_NAME = 'diorite'
PREFIX = '/usr/local'
PROJECT_INFO = {'appKeys': {u'MESSAGE_KEY_refreshrate': 10001, u'MESSAGE_KEY_simplemode': 10000}, u'watchapp': {u'watchface': False}, u'displayName': u'GoPro', u'uuid': u'f9963dc0-430a-4ee7-8814-ee4ab4bd9206', u'messageKeys': {u'MESSAGE_KEY_refreshrate': 10001, u'MESSAGE_KEY_simplemode': 10000}, 'companyName': u'Konrad Iturbe', u'enableMultiJS': True, u'sdkVersion': u'3', 'versionLabel': u'1.0', u'targetPlatforms': [u'aplite', u'basalt', u'chalk', u'diorite'], 'longName': u'GoPro', 'shortName': u'GoPro', u'resources': {u'media': [{u'menuIcon': True, u'type': u'bitmap', u'name': u'IMAGES_APP_ICON', u'file': u'images/app_icon.png'}, {u'type': u'bitmap', u'name': u'ICON_VIDEO_SIMPLE', u'file': u'images/video_icon.png'}, {u'type': u'bitmap', u'name': u'ICON_SETTINGS', u'file': u'images/settings_icon.png'}, {u'type': u'bitmap', u'name': u'ICON_VIDEO_TL', u'file': u'images/tlvideo_icon.png'}, {u'type': u'bitmap', u'name': u'ICON_VIDEO_LOOPING', u'file': u'images/looping_icon.png'}, {u'type': u'bitmap', u'name': u'ICON_VIDEO_DUAL', u'file': u'images/dual_icon.png'}, {u'type': u'bitmap', u'name': u'ICON_PHOTO_SIMPLE', u'file': u'images/photo_icon.png'}, {u'type': u'bitmap', u'name': u'ICON_PHOTO_CONTINUOUS', u'file': u'images/continuous_icon.png'}, {u'type': u'bitmap', u'name': u'ICON_PHOTO_NIGHTPHOTO', u'file': u'images/nightphoto_icon.png'}, {u'type': u'bitmap', u'name': u'ICON_MS_TIMELAPSE', u'file': u'images/timelapse_icon.png'}, {u'type': u'bitmap', u'name': u'ICON_MS_BURST', u'file': u'images/burst_icon.png'}, {u'type': u'bitmap', u'name': u'ICON_MS_NL', u'file': u'images/nightlapse_icon.png'}, {u'type': u'bitmap', u'name': u'IMAGE_LOGO_SPLASH', u'file': u'images/logo_splash.png'}, {u'type': u'bitmap', u'name': u'IMAGE_TILE_SPLASH', u'file': u'images/tile_splash.png'}, {u'type': u'font', u'name': u'MONO_FONT_14', u'file': u'fonts/UbuntuMono-Regular.ttf'}]}, 'name': u'GoPro'}
REQUESTED_PLATFORMS = [u'aplite', u'basalt', u'chalk', u'diorite']
RESOURCES_JSON = [{u'menuIcon': True, u'type': u'bitmap', u'name': u'IMAGES_APP_ICON', u'file': u'images/app_icon.png'}, {u'type': u'bitmap', u'name': u'ICON_VIDEO_SIMPLE', u'file': u'images/video_icon.png'}, {u'type': u'bitmap', u'name': u'ICON_SETTINGS', u'file': u'images/settings_icon.png'}, {u'type': u'bitmap', u'name': u'ICON_VIDEO_TL', u'file': u'images/tlvideo_icon.png'}, {u'type': u'bitmap', u'name': u'ICON_VIDEO_LOOPING', u'file': u'images/looping_icon.png'}, {u'type': u'bitmap', u'name': u'ICON_VIDEO_DUAL', u'file': u'images/dual_icon.png'}, {u'type': u'bitmap', u'name': u'ICON_PHOTO_SIMPLE', u'file': u'images/photo_icon.png'}, {u'type': u'bitmap', u'name': u'ICON_PHOTO_CONTINUOUS', u'file': u'images/continuous_icon.png'}, {u'type': u'bitmap', u'name': u'ICON_PHOTO_NIGHTPHOTO', u'file': u'images/nightphoto_icon.png'}, {u'type': u'bitmap', u'name': u'ICON_MS_TIMELAPSE', u'file': u'images/timelapse_icon.png'}, {u'type': u'bitmap', u'name': u'ICON_MS_BURST', u'file': u'images/burst_icon.png'}, {u'type': u'bitmap', u'name': u'ICON_MS_NL', u'file': u'images/nightlapse_icon.png'}, {u'type': u'bitmap', u'name': u'IMAGE_LOGO_SPLASH', u'file': u'images/logo_splash.png'}, {u'type': u'bitmap', u'name': u'IMAGE_TILE_SPLASH', u'file': u'images/tile_splash.png'}, {u'type': u'font', u'name': u'MONO_FONT_14', u'file': u'fonts/UbuntuMono-Regular.ttf'}]
RPATH_ST = '-Wl,-rpath,%s'
SANDBOX = False
SDK_VERSION_MAJOR = 5
SDK_VERSION_MINOR = 86
SHLIB_MARKER = None
SIZE = 'arm-none-eabi-size'
SONAME_ST = '-Wl,-h,%s'
STLIBPATH_ST = '-L%s'
STLIB_MARKER = None
STLIB_ST = '-l%s'
SUPPORTED_PLATFORMS = ['aplite', 'diorite', 'chalk', 'emery', 'basalt']
TARGET_PLATFORMS = ['diorite', 'chalk', 'basalt', 'aplite']
TIMESTAMP = 1483541970
USE_GROUPS = True
VERBOSE = 0
WEBPACK = '/home/konrad/.pebble-sdk/SDKs/current/node_modules/.bin/webpack'
cprogram_PATTERN = '%s'
cshlib_PATTERN = 'lib%s.so'
cstlib_PATTERN = 'lib%s.a'
macbundle_PATTERN = '%s.bundle'
