# rgame
Plugin for /r/game's Discord using the new Discord Slash commands.

## Usage

1. ```virtualenv env```
2. ```source env/bin/activate```
3. ```python -m pip -r requirements.txt```
4. Add all needed informations into "config.py"
     - In this case you only need to specify ```token = "YOUR DISCORD TOKEN"```
     - You should also remember to change ```test_guilds``` in main.py since Slash commands require discord to approve them which takes *way too much time* for global commands to be worth it
6. ```python main.py```

## License

This work is under the [European Union Public License v1.2](LICENSE) or – as soon they will be approved by the European Commission - subsequent versions of the EUPL (the "Licence");

You may get a copy of this license in your language from the European Commission [here](https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12).

Unless required by applicable law or agreed to in writing, software distributed under the Licence is distributed on an "AS IS" basis, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

See the Licence for the specific language governing permissions and limitations under the Licence.
