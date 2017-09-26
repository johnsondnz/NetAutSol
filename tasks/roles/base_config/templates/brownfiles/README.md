## Usage
* For non-abstracted configuration elements.
* Place files in here with matching `{{ inventory_hostname }}.txt`.
* base.j2 will automatically import these files
* Missing files are ignored.
* brownfile items should be progressively migrated to an abstracted state.
