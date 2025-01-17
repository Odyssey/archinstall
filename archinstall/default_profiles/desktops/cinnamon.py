from typing import TYPE_CHECKING, Any

from archinstall.default_profiles.profile import GreeterType, ProfileType
from archinstall.default_profiles.xorg import XorgProfile

if TYPE_CHECKING:
	_: Any


class CinnamonProfile(XorgProfile):
	def __init__(self) -> None:
		super().__init__('Cinnamon', ProfileType.DesktopEnv, description='')

	@property
	def packages(self) -> list[str]:
		return [
			"cinnamon",
			"system-config-printer",
			"gnome-keyring",
			"gnome-terminal",
			"blueman",
			"bluez-utils",
			"engrampa",
			"gnome-screenshot",
			"gvfs-smb",
			"xed",
			"xdg-user-dirs-gtk"
		]

	@property
	def default_greeter_type(self) -> GreeterType | None:
		return GreeterType.Lightdm
