# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# System
from typing import Optional, Union, List, Tuple, Callable

# Pip
from selenium_youtube import Youtube as SeleniumYoutube
from selenium_chrome import Chrome, ChromeAddonInstallSettings

from kproxy import Proxy

# -------------------------------------------------------------------------------------------------------------------------------- #



# -------------------------------------------------------- class: Youtube -------------------------------------------------------- #

class Youtube(SeleniumYoutube):

    # --------------------------------------------------------- Init --------------------------------------------------------- #

    def __init__(
        self,
        
        # profile
        profile_path: Optional[str] = None,
        profile_id: Optional[str] = None,

        # cookies
        pickle_cookies: bool = False,

        # proxy
        proxy: Optional[Union[Proxy, str]] = None,

        # addons
        addon_settings: Optional[List[ChromeAddonInstallSettings]] = None,

        # other paths
        chromedriver_path: Optional[str] = None,

        # chrome option settings
        private: bool = False,
        full_screen: bool = True,
        language: str = 'en-us',
        user_agent: Optional[str] = None,
        disable_images: bool = False,
        mute_audio: bool = False,

        screen_size: Optional[Tuple[int, int]] = None, # (width, height)
        headless: bool = False,
        home_page_url: Optional[str] = None,

        # selenium-wire support
        webdriver_class: Optional = None,

        # find function
        default_find_func_timeout: int = 2.5,
        
        # login
        prompt_user_input_login: bool = True,
        login_prompt_callback: Optional[Callable[[str], None]] = None,
        login_prompt_timeout_seconds: int = 60*5
    ):
        super().__init__(
            browser=Chrome(
                profile_path=profile_path,
                profile_id=profile_id,

                pickle_cookies=pickle_cookies,

                # proxy
                proxy=proxy,

                # addons
                addon_settings=addon_settings,

                # other paths
                chromedriver_path=chromedriver_path,

                # chrome option settings
                private=private,
                full_screen=full_screen,
                language=language,
                user_agent=user_agent,
                disable_images=disable_images,
                mute_audio=mute_audio,

                screen_size=screen_size,
                headless=headless,
                home_page_url=home_page_url,

                # selenium-wire support
                webdriver_class=webdriver_class,

                # find function
                default_find_func_timeout=default_find_func_timeout,
            ),
            prompt_user_input_login=prompt_user_input_login,
            login_prompt_callback=login_prompt_callback,
            login_prompt_timeout_seconds=login_prompt_timeout_seconds
        )


# -------------------------------------------------------------------------------------------------------------------------------- #