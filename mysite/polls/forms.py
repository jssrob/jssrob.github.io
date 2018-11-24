class SongListForm(ModelForm):
	class Meta:
		model = SongList
		fields = ['song']
